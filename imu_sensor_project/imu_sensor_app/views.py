from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import SensorData
from .getData import read_sensor_data

class SensorDataAPI(APIView):
    def post(self, request):
        sensor_data = read_sensor_data()  # Call your sensor data reading function

        if not sensor_data:
            return Response({"message": "No sensor data received"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            SensorData.objects.create(**sensor_data)  # Store the sensor data in the database
            return Response({"message": "Sensor data received and saved successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
