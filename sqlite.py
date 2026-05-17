import sqlite3

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

sql = """create table if not exist locations(
    ID integer primary key autoincrement,
    lat real,
    ion real,
    operator_reference text,
    country_reference text,
    postal_code text,
    number_of_evses integer
    )"""

cursor.execute(sql)
