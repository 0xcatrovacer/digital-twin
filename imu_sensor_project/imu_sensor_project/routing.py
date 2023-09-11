from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from imu_sensor_app.consumers import consumers

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/sensor_data/", consumers.SensorDataConsumer.as_asgi()),
        ])
    ),
})
