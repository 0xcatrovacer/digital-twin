from django.shortcuts import render
from .models import SensorData

def sensor_data(request):
    sensor_data = SensorData.objects.order_by('-timestamp').first()

    context = {
        'sensor_data': sensor_data,
    }

    return render(request, 'imu_sensor_app/sensor_data.html', context)
