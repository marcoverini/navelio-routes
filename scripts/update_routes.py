import pandas as pd
from scripts.utils import fetch_routes

def main():
    routes = fetch_routes()
    routes.to_csv("data/routes.csv", index=False)
    hubs = pd.DataFrame({
        "city": sorted(set(routes["origin_city"]) | set(routes["destination_city"]))
    })
    hubs.to_csv("data/hubs.csv", index=False)

if __name__ == "__main__":
    main()
