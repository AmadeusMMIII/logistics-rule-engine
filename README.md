# Smart Logistics Rule-Based AI Engine

An event-driven Rule Engine designed to ingest fleet telemetry and warehouse metrics to produce standardized, actionable real-time dashboard alerts.

## 📈 Architecture Pipeline
Vehicle/Inventory/Fleet Logs ──> Rule-Based Engine ──> Severity Matrix ──> JSON Payload API

## ⚙️ Rules Configurations
* **Overspeed:** Warning if > 80 km/h, Critical if > 95 km/h.
* **Low Stock:** Warning if < 20 units, Critical if < 5 units.
* **Idle Fleet:** Warning if > 3 hours inactive, Critical if > 7 hours.

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone [\[\[https://github.com/YOUR_USERNAME/logistics-rule-engine.git\](https://github.com/YOUR_USERNAME/logistics-rule-engine.git)\](https://github.com/AmadeusMMIII/logistics-rule-engine.git)](https://github.com/AmadeusMMIII/logistics-rule-engine.git)
   cd logistics-rule-engine

2. Run the application engine:
    ```bash
    python src/app.py
