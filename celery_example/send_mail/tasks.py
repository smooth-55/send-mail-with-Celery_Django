from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(*args, **kwargs):

    for mail in range(50):
        send_mail(
            "Subject(",
            "Random message...",
            "Your_mail@gmail.com",
            ["recipent_mail@gmail.com"],
        )
        print("sending....")
        
    return "mail has been sent successfully"
