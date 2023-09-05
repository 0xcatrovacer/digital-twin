from django.contrib import admin
from django.urls import path, include
from imu_sensor_app import views
from imu_sensor_app.views import SensorDataAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sensor_data, name='root'),  # Redirect root URL to sensor_data
    path('sensor_data/', views.sensor_data, name='sensor_data'),
    path('api/sensor-data/', SensorDataAPI.as_view(), name='sensor-data-api'),
]