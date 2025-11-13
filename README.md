# 🌍 Global Air Routes Dataset

This repository contains an automatically updated dataset of direct air routes between cities worldwide.  
The dataset includes details such as airline, origin, destination, and aircraft type.  

## Files
- `data/routes.csv` — list of routes.
- `data/hubs.csv` — list of city/airport hubs.
- `scripts/` — automation scripts to fetch and update data.
- `.github/workflows/update_routes.yml` — GitHub Actions workflow for automatic updates.

## Automation
The repository is designed to refresh data monthly using a GitHub Actions workflow.

## License
MIT License
