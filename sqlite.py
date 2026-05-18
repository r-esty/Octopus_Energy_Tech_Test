import sqlite3
import json

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

cursor.execute( """create table if not exists locations(
    ID integer primary key autoincrement,
    lat real,
    lon real,
    operator_reference text,
    country_reference text,
    postal_code text,
    number_of_evses integer)
    """)
    

cursor.execute( """create table if not exists eves(
    ID integer primary key autoincrement,
    physical_identifer text,
    status text)
    """)

cursor.execute( """create table if not exists connectors(
    ID integer primary key autoincrement,

    standard text,
    power integer)
    """)




with open('data/integrated.json') as f:
    locations = json.load(f)
    #print(locations)
    

    

    
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


connection.commit()
connection.close()

