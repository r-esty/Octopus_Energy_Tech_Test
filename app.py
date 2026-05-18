from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/locations")
def get_locations():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT ID, lat, lon, operator_reference, country_reference, postal_code FROM locations")
    rows = cur.fetchall()

    locations = []
    for row in rows:
        cur.execute("SELECT COUNT(*) FROM evses WHERE location_id = ?", (row["ID"],))
        evse_count = cur.fetchone()[0]

        locations.append({
            "coordinates": {
                "lat": row["lat"],
                "lon": row["lon"]
            },
            "operator_reference": row["operator_reference"],
            "country_reference": row["country_reference"],
            "postal_code": row["postal_code"],
            "number_of_evses": evse_count
        })

    conn.close()
    return jsonify({"locations": locations})

@app.route("/locations/<int:id>")
def get_location(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT ID, lat, lon, operator_reference, country_reference, postal_code FROM locations WHERE ID = ?", (id,))
    row = cur.fetchone()

    if not row:
        conn.close()
        return jsonify({"error": "Location not found"}), 404

    cur.execute("SELECT ID, physical_identifier, status FROM evses WHERE location_id = ?", (row["ID"],))
    evses = cur.fetchall()

    evse_list = []
    for evse in evses:
        cur.execute("SELECT standard, power FROM connectors WHERE evse_id = ?", (evse["ID"],))
        connectors = cur.fetchall()

        evse_list.append({
            "physical_identifier": evse["physical_identifier"],
            "status": evse["status"],
            "connectors": [{"standard": c["standard"], "power": c["power"]} for c in connectors]
        })

    conn.close()
    return jsonify({
        "coordinates": {
            "lat": row["lat"],
            "lon": row["lon"]
        },
        "operator_reference": row["operator_reference"],
        "country_reference": row["country_reference"],
        "postal_code": row["postal_code"],
        "evses": evse_list
    })

app.run()