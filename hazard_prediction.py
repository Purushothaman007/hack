import pandas as pd

# Load weather data from CSV (example with simplified columns)
weather_df = pd.read_csv('weather_data.csv')

def predict_hazard(iot_data, video_hazards, station_name="Abu"):
    """Predict hazards based on IoT, video, and weather data."""
    # Fetch weather data for the specific station
    station_weather = weather_df[weather_df['Station Name'] == station_name].iloc[0]

    # Temperature risk comparison
    if iot_data["temperature"] > station_weather["Mean Temperature in degree C - Maximum"]:
        return "High Temperature Risk"
    
    # Wind speed risk (strong winds may pose risks to workers and equipment)
    if iot_data["wind_speed"] > 25:
        return "High Wind Speed Risk"
    
    # Gas concentration risk (e.g., methane or CO2 leaks)
    if iot_data["gas_concentration"] > 75:
        return "High Gas Concentration Risk"
    
    # Humidity risk
    if iot_data["humidity"] > 85:
        return "High Humidity Risk"
    
    # Proximity to hazardous areas
    if iot_data["proximity_to_hazard"] < 2:
        return "High Proximity to Hazard Risk"
    
    # Video detection of potential hazards
    if video_hazards:
        return "Visual Hazard Detected"
    
    return "Safe"
