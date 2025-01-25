import random

def simulate_iot_data():
    """Simulate IoT sensor data for a construction site."""
    return {
        "seismic_activity": random.uniform(0, 5),
        "wind_speed": random.uniform(0, 30),
        "gas_concentration": random.uniform(0, 100),
        "temperature": random.uniform(15, 45),
        "humidity": random.uniform(30, 90),
        "proximity_to_hazard": random.uniform(0, 10),
    }
