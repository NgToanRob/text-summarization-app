import json
import os
import requests
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class FacebookWebhookView(View):
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
    PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Verify the webhook subscription
        if request.GET.get('hub.mode') == 'subscribe' and request.GET.get('hub.verify_token') == self.VERIFY_TOKEN:
            return HttpResponse(
                request.GET.get('hub.challenge'),
                content_type='text/plain',
                status=200
            )
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        # Parse the request body as JSON
        body = json.loads(request.body.decode('utf-8'))

        # Handle incoming messages
        for entry in body['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    self.send_message(
                        messaging_event['sender']['id'],
                        'Xin chào! Tôi có thể giúp gì được cho bạn?'
                    )

        return HttpResponse(status=200)

    def send_message(self, recipient_id, message_text):
        # Create the message payload
        message_data = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': message_text
            }
        }

        # Send the message using the Facebook Graph API
        response = requests.post(
            f'https://graph.facebook.com/v16.0/me/messages?access_token={self.PAGE_ACCESS_TOKEN}',
            json=message_data
        )
        response.raise_for_status()


class MessengerBotView(View):
    def get(self, request, *args, **kwargs):
        # Verify webhook by sending back challenge response
        if request.GET.get("hub.mode") == "subscribe" and request.GET.get("hub.challenge"):
            if request.GET.get("hub.verify_token") == os.environ.get('VERIFY_TOKEN'):
                return HttpResponse(request.GET["hub.challenge"])
            else:
                return HttpResponse("Verification token mismatch", status=403)

        return HttpResponse("Hello, world!", status=200)

    def post(self, request, *args, **kwargs):
        # Handle incoming messages and events from Facebook
        data = json.loads(request.body.decode("utf-8"))
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("postback"):
                        # Handle "Get Started" button postback event
                        if messaging_event["postback"].get("payload") == "GET_STARTED_PAYLOAD":
                            sender_id = messaging_event["sender"]["id"]
                            message_data = {
                                "recipient": {"id": sender_id},
                                "message": {
                                    "text": "Welcome to my bot! How can I help you today?",
                                    "quick_replies": [
                                        {
                                            "content_type": "text",
                                            "title": "Get weather",
                                            "payload": "GET_WEATHER_PAYLOAD"
                                        },
                                        {
                                            "content_type": "text",
                                            "title": "Get news",
                                            "payload": "GET_NEWS_PAYLOAD"
                                        }
                                    ]
                                }
                            }
                            self.send_message(message_data)

        return HttpResponse("OK", status=200)

    def send_message(data):
        # Send message to the user using the Messenger API
        response = requests.post(
            "https://graph.facebook.com/v11.0/me/messages",
            params={"access_token": os.environ.get('PAGE_ACCESS_TOKEN')},
            json=data
        )
        response.raise_for_status()
