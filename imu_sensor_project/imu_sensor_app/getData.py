### THIS IS NOT REQUIRED(PREPROCESSING)---> WE ARE DOING POSTPROCESSING(SENDING DATA DIRECTLY TO API AND PROCESSING IT)

import socket
import time
import requests

def read_sensor_data():
    # Replace this function with your actual sensor data reading logic.
    # It should return a dictionary with keys 'acceleration_x', 'acceleration_y', 'acceleration_z',
    # 'gyroscope_x', 'gyroscope_y', 'gyroscope_z', containing the sensor data.

    # For example:

    # Sample input string received from the STM32 board
    input_string = b"1.0 2.0 3.0 0.1 0.2 0.3".decode("utf-8")

    # Split the string into individual values
    values = input_string.split(" ")

    # Define keys for the dictionary
    keys = ['acceleration_x', 'acceleration_y', 'acceleration_z', 'gyroscope_x', 'gyroscope_y', 'gyroscope_z']

    # Create a dictionary by pairing keys with values
    sensor_data = {key: float(value) for key, value in zip(keys, values)}

    print(sensor_data)
    # sensor_data = {
    #     'acceleration_x': 1.0,
    #     'acceleration_y': 2.0,
    #     'acceleration_z': 3.0,
    #     'gyroscope_x': 0.1,
    #     'gyroscope_y': 0.2,
    #     'gyroscope_z': 0.3,
    # }
    return sensor_data

# # Configure the UDP server address and port
# UDP_SERVER_IP = "0.0.0.0"  # Replace with the IP of your laptop
# UDP_SERVER_PORT = 12345  # Use the same port as the server

# # Initialize a UDP socket
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     try:
#         # Read sensor data
#         sensor_data = read_sensor_data()

#         # Push the data to the Django app via HTTP POST request
#         response = requests.post('http://127.0.0.1:8000/api/sensor_data/', data=sensor_data)

#         # Store the data in the SQLite database (you can use Django ORM here)
#         # Example: sensor_data = SensorData.objects.create(**sensor_data)

#         # Sleep to control the data collection rate
#         time.sleep(1)  # Adjust as needed
#     except KeyboardInterrupt:
#         break

# # Close the UDP socket when done
# udp_socket.close()