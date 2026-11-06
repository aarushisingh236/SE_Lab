import math


def parse_walk_schedule(schedule_spec):
    try:
        if not isinstance(schedule_spec, str):
            return None

        parts = schedule_spec.strip().split("-")
        if len(parts) != 3:
            return None

        pets_str, mins_str, weekend_str = parts
        pets = int(pets_str.strip())
        mins = int(mins_str.strip())
        weekend = weekend_str.strip().upper()

        if pets <= 0 or mins <= 0:
            return None

        weekend_map = {"YES": 15.0, "NO": 0.0}
        if weekend not in weekend_map:
            return None

        weekend_fee = weekend_map[weekend]
        base_fee = 20.0 if mins <= 30 else 35.0
        total = base_fee + (pets * 5.0) + weekend_fee

        return f"Walk: {pets} pets, {mins} mins - Total ${total:.2f}"

    except (ValueError, TypeError, AttributeError):
        return None


def compute_pace_per_pet(walk_metrics_str):
    try:
        if not isinstance(walk_metrics_str, str):
            return None

        parts = walk_metrics_str.split("/")
        if len(parts) != 2:
            return None

        mins_str, pets_str = parts
        mins = float(mins_str.strip())
        pets = float(pets_str.strip())

        if not math.isfinite(mins) or not math.isfinite(pets):
            return None

        if mins < 0 or pets <= 0:
            return None

        pace = mins / pets
        return round(pace, 2)

    except (ValueError, TypeError, ZeroDivisionError, AttributeError):
        return None


def lookup_temperament_surcharge(temperament_code):
    if not isinstance(temperament_code, str):
        return None

    surcharges = {
        "CAL": 0.0,
        "PLA": 5.0,
        "REA": 12.0,
        "AGG": 20.0
    }

    prefix = temperament_code.strip().upper()[:3]
    return surcharges.get(prefix)


def main():
    print("==== Running parse_walk_schedule ====")
    s_input = input("Enter schedule (e.g. 2-30-YES): ")
    print(parse_walk_schedule(s_input))

    print("\n==== Running compute_pace_per_pet ====")
    p_input = input("Enter minutes/pets (e.g. 45/3): ")
    print("Pace (min/pet):", compute_pace_per_pet(p_input))

    print("\n==== Running lookup_temperament_surcharge ====")
    t_input = input(
        "Enter temperament code (e.g. CALM, PLAYFUL, AGGRESSIVE): "
    )
    print("Surcharge: $", lookup_temperament_surcharge(t_input))


if __name__ == "__main__":
    main()
