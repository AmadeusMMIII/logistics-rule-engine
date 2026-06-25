def process_rules(vehicles, inventory, fleet):
    alerts = []

    # Overspeed Rules
    for v in vehicles:
        if v["speed"] > 80:
            severity = "CRITICAL" if v["speed"] > 95 else "WARNING"
            alerts.append({"type": "OVERSPEED", "severity": severity, "entity_id": v["vehicle"], "metric_value": v["speed"]})

    # Inventory Rules
    for item in inventory:
        if item["stock"] < 20:
            severity = "CRITICAL" if item["stock"] < 5 else "WARNING"
            alerts.append({"type": "LOW_STOCK", "severity": severity, "entity_id": item["item"], "metric_value": item["stock"]})

    # Idle Rules
    for truck in fleet:
        if truck["idle_hours"] > 3.0:
            severity = "CRITICAL" if truck["idle_hours"] > 7.0 else "WARNING"
            alerts.append({"type": "IDLE_FLEET", "severity": severity, "entity_id": truck["vehicle"], "metric_value": truck["idle_hours"]})

    return alerts