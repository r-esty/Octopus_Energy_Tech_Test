# Octopus Tech Test - Backend Engineer

## How to install and run

1. Install dependencies: `pip install -r requirements.txt`
2. Load data into database: `python sqlite.py`
3. Start the API: `python app.py`
4. Visit `http://127.0.0.1:5000/locations` or `http://127.0.0.1:5000/locations/<id>`
5. Run tests: `python test_app.py`

## Endpoints

- `GET /locations` - returns a list of all locations with coordinates, operator, country, postal code, and EVSE count
- `GET /locations/<id>` - returns a single location with nested EVSEs and connectors

## Approach and notes

- Chose SQLite for its simplicity and prior experience from a previous project (https://github.com/r-esty/Clash_Royale_Trophies_Bot)
- Modelled the data across three tables (locations, evses, connectors) linked with foreign keys
- Used Flask to expose the data as a REST API as it integrates well with SQLite and is lightweight
- Realised partway through that I needed foreign keys (location_id on evses, evse_id on connectors) to link the tables together for the detail endpoint
- Used `.get()` with default values when extracting JSON, as some fields were inconsistent (e.g. operator was sometimes a dict, sometimes None)
- Wrote two tests: one for data persistence, one for the API endpoint
- Work was spread across the day with breaks in between, not done in one continuous sitting

## Resources used

- https://www.youtube.com/watch?v=jsX99U8UkOo - SQLite database creation
- https://www.youtube.com/watch?v=eD2oAsalw7E - inserting rows and columns
- https://stackoverflow.com/questions/20199126/reading-json-from-a-file - reading JSON in Python
- Used AI (Claude) for explaining concepts such as foreign keys, JSON insertion patterns, and choosing Flask for the API layer
- Used AI for help with README structure

## TODO (with more time)

- Add filtering by country and operator
- Add ordering by proximity to given coordinates
- Integrate the supplementing.json data source
- Add more comprehensive test coverage
- Dockerise the application for easier local setup
- Set up a CI/CD pipeline to run tests automatically on push