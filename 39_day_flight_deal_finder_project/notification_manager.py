from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, sid, auth_token, phone_num, sms_body):
        self.sid = sid
        self.auth_token = auth_token
        self.phone_num = phone_num
        self.sms_body = sms_body

    def send_sms(self):
        client = Client(self.sid, self.auth_token)

        message = client.messages.create(
            from_='+12055824835',
            body=self.sms_body,
            to='+998998205414'
        )

        print(message.sid)
