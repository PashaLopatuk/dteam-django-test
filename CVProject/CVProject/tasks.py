from io import BytesIO
from celery import shared_task
from django.core.mail import EmailMessage

from utils.config import CeleryConfig
from utils.temporary_files import read_temp_bin_file

@shared_task
def send_pdf_to_email(email: str, pdf_file_id: str, title="document", description=""):
    print({
        "subject":f"Your PDF File {title}",
        "body":description,
        "from_email":CeleryConfig.author_email,
        "to":[email],
    })
    
    mail = EmailMessage(
        subject=f"Your PDF File {title}",
        body=description,
        from_email=CeleryConfig.author_email,
        to=[email],
    )
    file = read_temp_bin_file(file_id=pdf_file_id)
    
    print(898989)
    mail.attach(title, file, "application/pdf")
    
    mail.send()
