import json
import os
from generator import generate_logistics_data
from engine import process_rules

def main():
    print("Initializing Rule-Based AI Engine...")
    
    # 1. Fetch synthetic dataset
    vehicles, inventory, fleet = generate_logistics_data()
    
    # 2. Run rule execution
    triggered_alerts = process_rules(vehicles, inventory, fleet)
    
    # 3. Ensure the output 'data/' folder exists
    os.makedirs("data", exist_ok=True)
    
    # 4. Save the full Alert Logs to a file
    with open("data/triggered_alerts.json", "w") as f:
        json.dump(triggered_alerts, f, indent=4)
        
    # 5. Save the raw mock data pool (Optional, for reference)
    mock_raw_data = {
        "vehicles": vehicles,
        "inventory": inventory,
        "fleet": fleet
    }
    with open("data/mock_data.json", "w") as f:
        json.dump(mock_raw_data, f, indent=4)
    
    print("\n[SUCCESS] Pipeline execution complete.")
    print(f"-> Saved {len(triggered_alerts)} actionable alerts to 'data/triggered_alerts.json'")
    print("-> Saved raw historical records to 'data/mock_data.json'")

if __name__ == "__main__":
    main()