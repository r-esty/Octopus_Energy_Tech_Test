import sqlite3
from app import app

def test_locations_exist():
    conn = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM locations")
    count = cur.fetchone()[0]
    assert count > 0
    conn.close()

def test_locations_endpoint():
    client = app.test_client()
    response = client.get("/locations")
    assert response.status_code == 200
    data = response.get_json()
    assert "locations" in data
    assert len(data["locations"]) > 0

test_locations_exist()
test_locations_endpoint()
print("All tests passed")