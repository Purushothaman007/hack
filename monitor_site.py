import time
import threading
from iot_simulation import simulate_iot_data
from video_processing import process_video
from hazard_prediction.py import predict_hazard
from lora_communication import send_alert_to_hospital

def monitor_site(video_path, lora_port, station_name="Abu"):
    """Main function to monitor the construction site."""
    video_queue = []

    # Run video analytics in a separate thread
    video_thread = threading.Thread(target=process_video, args=(video_path, video_queue))
    video_thread.start()

    while True:
        iot_data = simulate_iot_data()  # Get IoT data from sensors
        video_hazards = video_queue.pop(0) if video_queue else []  # Get video hazards

        # Predict hazards based on the IoT, video, and weather data
        hazard_status = predict_hazard(iot_data, video_hazards, station_name)
        print(f"IoT Data: {iot_data}")
        print(f"Video Hazards: {video_hazards}")
        print(f"Hazard Prediction: {hazard_status}")

        # Alert if a hazard is detected
        if hazard_status != "Safe":
            print("ALERT! Immediate action required.")
            # Send alert to the hospital or relevant authorities via LoRa communication
            send_alert_to_hospital(lora_port, hazard_status)

        time.sleep(1)  # Simulate real-time updates

    # Wait for video processing thread to complete
    video_thread.join()

if __name__ == "__main__":
    video_path = "construction_site.mp4"  # Replace with your video file or camera feed
    lora_port = 'COM4'  # Change this to the correct port where the LoRa module is connected
    monitor_site(video_path, lora_port, station_name="Abu")  # You can change the station name based on your location
