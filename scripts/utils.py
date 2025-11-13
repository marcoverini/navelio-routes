import pandas as pd

def fetch_routes():
    # Placeholder: later we'll connect to a data source (e.g. OpenFlights, etc.)
    routes = pd.DataFrame([
        {"origin_city": "London", "origin_country": "UK",
         "destination_city": "New York", "destination_country": "USA",
         "airline": "British Airways", "aircraft": "B777"},
        {"origin_city": "Paris", "origin_country": "France",
         "destination_city": "Tokyo", "destination_country": "Japan",
         "airline": "Air France", "aircraft": "B787"},
    ])
    return routes
