from django.http import HttpResponse

class StripeWH_Handler:
    def __init__(self, request):
        self.request = request
    # Handle a generic/unknow/unexpected webhook event
    def handle_event(self, event):
        return HttpResponse(
            content=f"Webhook received: {event["type"]}",
            status=200)
    # Handle the payment intent succeeded webhook.
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        return HttpResponse(
            content=f"Webhook received: {event["type"]}",
            status=200)
    # Handle the payment intent failed webhook.
    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f"Webhook received: {event["type"]}",
            status=200)
