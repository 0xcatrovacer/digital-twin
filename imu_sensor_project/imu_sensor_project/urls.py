from django.contrib import admin
from django.urls import path, include
from imu_sensor_app import views
from imu_sensor_app.views import SensorDataAPI

urlpatterns = [
    path('api/sensor-data/', SensorDataAPI.as_view(), name='sensor-data-api'),
    path('admin/', admin.site.urls),
    path('', views.SensorData, name='root'),  # Redirect root URL to sensor_data
    path('sensor_data/', views.SensorData, name='sensor_data'),
]
