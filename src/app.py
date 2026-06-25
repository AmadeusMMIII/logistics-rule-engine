import json
from generator import generate_logistics_data
from engine import process_rules

def main():
    print("Initializing Rule-Based AI Engine...")
    
    # 1. Fetch synthetic dataset
    vehicles, inventory, fleet = generate_logistics_data()
    
    # 2. Run rule execution
    triggered_alerts = process_rules(vehicles, inventory, fleet)
    
    # 3. Output JSON Dashboard feed
    print(json.dumps(triggered_alerts[:5], indent=4))
    print(f"\nPipeline execution successful. Total alerts generated: {len(triggered_alerts)}")

if __name__ == "__main__":
    main()