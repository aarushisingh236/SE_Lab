import pytest

from pet_walking_service import (
    process_walking_routes,
    inspect_gps_collars
)


# 1. Invalid routes input
def test_invalid_routes():
    with pytest.raises(ValueError):
        process_walking_routes("invalid", 5.0)


# 2. Negative transport fee
def test_negative_transport_fee():
    with pytest.raises(ValueError):
        process_walking_routes([], -5.0)


# 3. Unconfirmed routes are skipped
def test_unconfirmed_route():
    routes = [
        {
            "route_confirmed": False,
            "session_type": "standard_30",
            "walks": [{"num_pets": 2}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 4. Test all supported session types
def test_all_session_types():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_60",
            "walks": [{"num_pets": 1}]
        },
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [{"num_pets": 1}]
        },
        {
            "route_confirmed": True,
            "session_type": "express_15",
            "walks": [{"num_pets": 1}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 86.0
    assert result["status"] == "COMPLETED"


# 5. Unknown session type
def test_unknown_session_type():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "premium_90",
            "walks": [{"num_pets": 1}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 6. Default session type and default walks
def test_default_route_values():
    routes = [
        {
            "route_confirmed": True
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 7. Invalid pet count
def test_invalid_pet_count():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [
                {"num_pets": 0},
                {"num_pets": -1},
                {"num_pets": 1}
            ]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 27.0
    assert result["status"] == "COMPLETED"


# 8. More than three pets receive a discount
def test_more_than_three_pets():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [{"num_pets": 4}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 48.6
    assert result["status"] == "COMPLETED"


# 9. Aggression alert during standard 30-minute session
def test_aggression_alert_standard_30():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [
                {
                    "num_pets": 2,
                    "aggression_alert": True,
                    "needs_meds": True
                }
            ]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 6.0
    assert result["status"] == "COMPLETED"


# 10. Aggression alert during standard 60-minute session
def test_aggression_alert_standard_60():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_60",
            "walks": [
                {"num_pets": 2},
                {
                    "num_pets": 1,
                    "aggression_alert": True,
                    "needs_meds": True
                },
                {"num_pets": 3}
            ]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 11. Medication fee
def test_medication_fee():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "express_15",
            "walks": [
                {
                    "num_pets": 2,
                    "needs_meds": True
                }
            ]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 30.0
    assert result["status"] == "COMPLETED"


# 12. Weekend transport fee
def test_weekend_transport_fee():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "is_weekend": True,
            "walks": [{"num_pets": 1}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 32.0
    assert result["status"] == "COMPLETED"


# 13. More than four incidents trigger audit
def test_incident_audit():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [{"num_pets": 0} for _ in range(5)]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "INCIDENT_AUDIT"


# 14. Empty GPS data
def test_empty_gps_data():
    assert inspect_gps_collars([]) == "NO_DATA"


# 15. Two consecutive weak signals
def test_consecutive_weak_signals():
    collar_matrix = [
        [50, 15, 10, 60]
    ]

    assert inspect_gps_collars(collar_matrix) == "LOST_SIGNAL_ALERT"


# 16. GPS signal recovery resets the streak
def test_gps_signal_recovery():
    collar_matrix = [
        [15, 25, 18, 30]
    ]

    assert inspect_gps_collars(collar_matrix) == "ONLINE"


# 17. Normal GPS readings
def test_gps_online():
    collar_matrix = [
        [80, 70, 60],
        [90, 85, 75]
    ]

    assert inspect_gps_collars(collar_matrix) == "ONLINE"

# 18. Empty routes list
def test_empty_routes():
    result = process_walking_routes([], 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 19. Confirmed route with no walks
def test_confirmed_route_without_walks():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": []
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_EARNINGS"


# 20. GPS collar with an empty log
def test_empty_collar_log():
    collar_matrix = [[]]

    assert inspect_gps_collars(collar_matrix) == "ONLINE"


# 21. One weak signal is not enough to trigger an alert
def test_single_weak_signal():
    collar_matrix = [
        [15, 30, 10]
    ]

    assert inspect_gps_collars(collar_matrix) == "ONLINE"


# 22. Exactly three pets should not receive the discount
def test_exactly_three_pets():
    routes = [
        {
            "route_confirmed": True,
            "session_type": "standard_30",
            "walks": [{"num_pets": 3}]
        }
    ]

    result = process_walking_routes(routes, 5.0)

    assert result["total_revenue"] == 37.0
    assert result["status"] == "COMPLETED"


# 23. Multiple collar logs are checked independently
def test_multiple_collar_logs():
    collar_matrix = [
        [10],
        [15, 12]
    ]

    assert inspect_gps_collars(collar_matrix) == "LOST_SIGNAL_ALERT"
