import sqlite3
import json

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")
cursor = connection.cursor()

cursor.execute("""create table if not exists locations(
    ID integer primary key autoincrement,
    lat real,
    lon real,
    operator_reference text,
    country_reference text,
    postal_code text,
    number_of_evses integer)
    """)

cursor.execute("""create table if not exists evses(
    ID integer primary key autoincrement,
    physical_identifier text,
    status text)
    """)

cursor.execute("""create table if not exists connectors(
    ID integer primary key autoincrement,
    standard text,
    power integer)
    """)

with open('data/integrated.json') as f:
    locations = json.load(f)

for location in locations:
    operator = str(location.get("operator") or "")
    country = str(location.get("country") or "")

    cursor.execute(
        "INSERT INTO locations (lat, lon, operator_reference, country_reference, postal_code) VALUES (?, ?, ?, ?, ?)",
        (
            location["coordinates"]["latitude"],
            location["coordinates"]["longitude"],
            operator,
            country,
            location["postal_code"]
        )
    )
    location_id = cursor.lastrowid

    for evse in location["evses"]:
        cursor.execute(
            "INSERT INTO evses (physical_identifier, status) VALUES (?, ?)",
            (evse["physical_reference"], evse["status"])
        )
        evse_id = cursor.lastrowid

        for connector in evse["connectors"]:
            cursor.execute(
                "INSERT INTO connectors (standard, power) VALUES (?, ?)",
                (connector.get("standard", ""), connector.get("max_electric_power", 0))
            )

connection.commit()
connection.close()