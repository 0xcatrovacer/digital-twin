from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("sensor_data_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("sensor_data_group", self.channel_name)

    async def send_sensor_data(self, event):
        await self.send(json.dumps(event["data"]))
