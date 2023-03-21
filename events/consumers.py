import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MandrillConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("mandrill", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("mandrill", self.channel_name)

    async def send_notification(self, event):
        event_type = event["event_type"]
        msg_id = event["msg_id"]
        subject = event["subject"]
        sender = event["sender"]
        email = event["email"]
        message = event["message"]
        await self.send(
            text_data=json.dumps(
                {
                    "event_type": event_type,
                    "msg_id": msg_id,
                    "subject": subject,
                    "sender": sender,
                    "email": email,
                    "message": message,
                }
            )
        )
