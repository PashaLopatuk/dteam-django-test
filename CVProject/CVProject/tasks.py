from io import BytesIO
from celery import shared_task
from django.core.mail import EmailMessage

from utils.config import CeleryConfig

@shared_task
def send_pdf_to_email(email: str, pdf_file: BytesIO, title="document", description=""):
    mail = EmailMessage(
        subject=f"Your PDF File {title}",
        body=description,
        from_email=CeleryConfig.author_email,
        to=[email],
    )
    mail.attach(title, pdf_file.read(), "application/pdf")
    
    mail.send()
