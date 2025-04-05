from io import BytesIO
from celery import shared_task
from django.core.mail import EmailMessage

from utils.config import CeleryConfig
from utils.temporary_files import get_temp_file_name, read_temp_bin_file

@shared_task
def send_pdf_to_email(email: str, pdf_file_id: str, title="document", description=""):    
    print(f'{pdf_file_id=}')
    mail = EmailMessage(
        subject=f"Your PDF File {title}",
        body=description,
        from_email=CeleryConfig.author_email,
        to=[email],
    )
    pdf_file_path = get_temp_file_name(file_id=pdf_file_id, file_ext=".pdf")
    mail.attach_file(pdf_file_path)
    
    mail.send()
