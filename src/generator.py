import random

def generate_logistics_data(seed=42):
    random.seed(seed)
    item_categories = ["Rice", "Milk", "Medicine", "Water", "Flour", "Oil", "Sugar", "Coffee"]
    truck_ids = [f"TRK{str(i).zfill(3)}" for i in range(1, 201)]
    
    vehicles = []
    inventory = []
    fleet = []

    # Telemetry
    for truck in truck_ids[:150]:
        speed = random.randint(50, 79) if random.random() > 0.15 else random.randint(81, 110)
        vehicles.append({"vehicle": truck, "speed": speed})

    # Warehouse
    for i in range(150):
        item_name = f"{random.choice(item_categories)} #{random.randint(100, 999)}"
        stock = random.randint(20, 150) if random.random() > 0.10 else random.randint(1, 19)
        inventory.append({"item": item_name, "stock": stock})

    # Idle Fleet
    for truck in truck_ids:
        idle_hours = round(random.uniform(0.0, 2.5), 1) if random.random() > 0.20 else round(random.uniform(3.1, 12.0), 1)
        fleet.append({"vehicle": truck, "idle_hours": idle_hours})

    return vehicles, inventory, fleet