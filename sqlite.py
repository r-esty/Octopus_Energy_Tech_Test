import sqlite3
import json

connection = sqlite3.connect("locations.db")
cursor = connection.cursor()

cursor.execute("""create table if not exists locations(
    ID integer primary key autoincrement,
    lat real,
    lon real,
    operator_reference text,
    country_reference text,
    postal_code text)
    """)

cursor.execute("""create table if not exists evses(
    ID integer primary key autoincrement,
    location_id integer,
    physical_identifier text,
    status text,
    foreign key (location_id) references locations(ID))
    """)

cursor.execute("""create table if not exists connectors(
    ID integer primary key autoincrement,
    evse_id integer,
    standard text,
    power integer,
    foreign key (evse_id) references evses(ID))
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
            "INSERT INTO evses (location_id, physical_identifier, status) VALUES (?, ?, ?)",
            (location_id, evse.get("physical_reference", ""), evse.get("status", ""))
        )
        evse_id = cursor.lastrowid

        for connector in evse["connectors"]:
            cursor.execute(
                "INSERT INTO connectors (evse_id, standard, power) VALUES (?, ?, ?)",
                (evse_id, connector.get("standard", ""), connector.get("max_electric_power", 0))
            )

connection.commit()
connection.close()