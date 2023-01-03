from twilio.rest import Client


def send_sms(message, phone):
    """Send SMS message to user."""
    account_sid = "YOUR TWILIO ACCOUNT SID"
    auth_token = "YOUR TWILIO AUTH TOKEN"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="YOUR TWILIO PHONE NUMBER",
        to=f"{phone}"
    )
