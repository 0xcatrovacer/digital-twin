import serial
import time
import requests

def read_sensor_data():
    # It should return a dictionary with keys 'acceleration_x', 'acceleration_y', 'acceleration_z',
    # 'gyroscope_x', 'gyroscope_y', 'gyroscope_z', containing the sensor data.

    # For example:
    sensor_data = {
        'acceleration_x': 1.0,
        'acceleration_y': 2.0,
        'acceleration_z': 3.0,
        'gyroscope_x': 0.1,
        'gyroscope_y': 0.2,
        'gyroscope_z': 0.3,
    }
    return sensor_data

# Initialize serial communication with the sensor
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)  # Adjust the port and baud rate accordingly

while True:
    try:
        # Read sensor data
        sensor_data = read_sensor_data()

        # Push the data to the Django app via HTTP POST request
        response = requests.post('http://127.0.0.1:8000/api/sensor_data/', data=sensor_data)

        # Store the data in the SQLite database (you can use Django ORM here)
        # Example: sensor_data = SensorData.objects.create(**sensor_data)

        # Sleep to control the data collection rate
        time.sleep(1)  # Adjust as needed
    except KeyboardInterrupt:
        break

# Close the serial port when done
ser.close()
