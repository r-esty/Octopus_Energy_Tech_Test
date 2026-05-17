import sqlite3

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

sql = """create table locations(
    ID integer primary key autoincrement,
    lat real,
    ion real,
    operator_reference text,
    country_reference text,
    postal_code text,
    number_of_evses integer
    )"""

cursor.execute(sql)


connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

sql_1 = """create table eves(
    ID integer primary key autoincrement,
    physical_identifer text,
    status text
    )"""

cursor.execute(sql_1)

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

sql_2 = """create table connectors(
    ID integer primary key autoincrement,

    standard text,
    power integer
    )"""

cursor.execute(sql_2)

