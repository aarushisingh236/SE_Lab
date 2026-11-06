from hypothesis import given, strategies as st
from processor import (
    parse_walk_schedule,
    compute_pace_per_pet,
    lookup_temperament_surcharge
)


# Property-based fuzz tests

@given(st.text() | st.none())
def test_parse_walk_schedule_no_crash(s):
    try:
        parse_walk_schedule(s)
    except Exception as e:
        assert False, f"parse_walk_schedule crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_compute_pace_per_pet_safe(s):
    try:
        compute_pace_per_pet(s)
    except Exception as e:
        assert False, f"compute_pace_per_pet crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_lookup_temperament_surcharge_safe(s):
    try:
        lookup_temperament_surcharge(s)
    except Exception as e:
        assert False, f"lookup_temperament_surcharge crashed with input {s!r}: {e}"


# Additional functional and validation tests

def test_parse_walk_schedule_valid():
    assert parse_walk_schedule("2-30-YES") == (
        "Walk: 2 pets, 30 mins - Total $45.00"
    )


def test_parse_walk_schedule_invalid():
    invalid_inputs = [
        None, "", "2-30", "abc-30-YES",
        "0-30-YES", "2-0-YES", "2-30-MAYBE"
    ]
    for value in invalid_inputs:
        assert parse_walk_schedule(value) is None


def test_compute_pace_valid():
    assert compute_pace_per_pet("45/3") == 15.0
    assert compute_pace_per_pet("30/2") == 15.0


def test_compute_pace_invalid():
    invalid_inputs = [
        None, "", "/", "45/0", "-5/2",
        "abc/2", "45/2/3", "nan/2", "inf/2"
    ]
    for value in invalid_inputs:
        assert compute_pace_per_pet(value) is None


def test_lookup_temperament_valid():
    assert lookup_temperament_surcharge("CALM") == 0.0
    assert lookup_temperament_surcharge("PLAYFUL") == 5.0
    assert lookup_temperament_surcharge("REACTIVE") == 12.0
    assert lookup_temperament_surcharge("AGGRESSIVE") == 20.0


def test_lookup_temperament_invalid():
    invalid_inputs = [None, "", "UNKNOWN", "XYZ"]
    for value in invalid_inputs:
        assert lookup_temperament_surcharge(value) is None
