
"""Pharmacy stock and prescription management system."""

#PES2UG24CS015

import json
import sqlite3
from datetime import datetime

conn = sqlite3.connect(":memory:")
stock = {}
prescriptions = []


def setup_database():
    """Create and populate the patients database."""
    cur = conn.cursor()
    cur.execute("CREATE TABLE patients (id TEXT, name TEXT, allergy TEXT)")
    cur.execute("INSERT INTO patients VALUES ('P1', 'Kavya', 'penicillin')")
    cur.execute("INSERT INTO patients VALUES ('P2', 'Arjun', 'none')")
    cur.execute("INSERT INTO patients VALUES ('P3', 'Meena', 'ibuprofen')")
    conn.commit()


def find_patient(name):
    """Find a patient by name."""
    cur = conn.cursor()
    query = "SELECT id, allergy FROM patients WHERE name = ?"
    return cur.execute(query, (name,)).fetchall()


def add_stock(drug, units, expiry, batch_log=None):
    """Add drug units to stock and record the batch."""
    if batch_log is None:
        batch_log = []
    stock[drug] = {
        "units": stock.get(drug, {}).get("units", 0) + units,
        "expiry": expiry,
    }
    batch_log.append((drug, units))
    return len(batch_log)


def dispense(patient_name, drug, units):
    """Dispense medication if the patient has no matching allergy."""
    try:
        patient = find_patient(patient_name)[0]
        if drug.lower() in patient[1].lower():
            print("Allergy warning for", patient_name)
            return False
        if drug not in stock or stock[drug]["units"] < units:
            return False
        stock[drug]["units"] -= units
        prescriptions.append({
            "patient": patient[0],
            "drug": drug,
            "units": units,
            "time": str(datetime.now()),
        })
        return True
    except (IndexError, KeyError, TypeError, sqlite3.Error):
        return False


def expiring_soon(days=30):
    """Return drugs expiring within the specified number of days."""
    soon = []
    now = datetime.now()
    for drug, details in stock.items():
        expiry = datetime.strptime(details["expiry"], "%Y-%m-%d")
        if 0 <= (expiry - now).days < days:
            soon.append(drug)
    return soon


def export_prescriptions(file="prescriptions.json"):
    """Export prescriptions to a JSON file."""
    with open(file, "w", encoding="utf-8") as prescription_file:
        json.dump(prescriptions, prescription_file, indent=2)


def load_stock(file="stock.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as stock_file:
            loaded_stock = json.load(stock_file)
        if isinstance(loaded_stock, dict):
            stock.clear()
            stock.update(loaded_stock)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load stock from {file}: {error}")


def print_stock():
    """Print the current pharmacy stock."""
    print("Pharmacy Stock")
    for drug, details in stock.items():
        print(
            f"{drug} -> {details['units']} units, "
            f"expires {details['expiry']}"
        )


def main():
    """Run the pharmacy stock management demonstration."""
    setup_database()
    load_stock()
    add_stock("Paracetamol", 100, "2027-03-01")
    add_stock("Amoxicillin", 20, "2025-12-31")
    add_stock("Penicillin", 50, "2027-01-15")
    add_stock("Ibuprofen", -15, "2026-11-30")
    print("Arjun gets Amoxicillin:", dispense("Arjun", "Amoxicillin", 30))
    print("Kavya gets Penicillin:", dispense("Kavya", "Penicillin", 10))
    print("Meena gets ibuprofen:", dispense("Meena", "ibuprofen", 2))
    print("Unknown patient:", dispense("Ghost", "Paracetamol", 5))
    name = input("Patient name to look up (Enter for Arjun): ") or "Arjun"
    print("Lookup result:", find_patient(name))
    print("Expiring within 30 days:", expiring_soon())
    export_prescriptions()
    print_stock()


if __name__ == "__main__":
    main()
