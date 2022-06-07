from django.core.mail import EmailMessage
from .tasks import email_sender


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email_sender.delay(email)