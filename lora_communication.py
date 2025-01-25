import serial
import time

def initialize_lora(port):
    """Initialize the LoRa communication."""
    try:
        lora = serial.Serial(port, baudrate=9600, timeout=1)
        print(f"LoRa module initialized on {port}")
        return lora
    except Exception as e:
        print(f"Error initializing LoRa: {e}")
        return None

def send_alert_to_hospital(port, alert_message):
    """Send an alert message to the hospital using LoRa."""
    lora = initialize_lora(port)
    if lora:
        try:
            # Send the alert message to the hospital via LoRa
            lora.write(alert_message.encode())  # Encoding the message before sending
            print(f"Alert sent to hospital: {alert_message}")
            time.sleep(2)  # Allow some time for the message to be sent
        except Exception as e:
            print(f"Error sending alert: {e}")
        finally:
            lora.close()  # Close the serial connection

if __name__ == "__main__":
    port = "COM4"  # Example port, change it as needed
    alert_message = "ALERT! High Temperature Risk at construction site."
    send_alert_to_hospital(port, alert_message)
