# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from imu_sensor_app.consumers import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imu_sensor_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            path("ws/sensor_data/", consumers.SensorDataConsumer.as_asgi()),
        )
    ),
})
