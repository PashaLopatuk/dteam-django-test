from io import BytesIO
import os
from typing import Any, Optional
from uuid import uuid4

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


from xhtml2pdf import pisa

from utils.temporary_files import get_temp_file_name
from utils.temporary_files import temp_files_dir


class DjangoPdfResolver:
    async def render_pdf(
        self,
        template_path: str,
        template_context: dict[str, Any],
    ) -> BytesIO:
        result_file = BytesIO()

        template = get_template(template_path)
        html = template.render(template_context)

        pisa.pisaDocument(BytesIO(html.encode()), result_file)

        return result_file
        
    def create_temp_pdf_file(
        self,
        template_path: str,
        template_context: dict[str, Any],
    ) -> str:
        template = get_template(template_path)
        html = template.render(template_context)
        file_id = str(uuid4())
        file_dest = get_temp_file_name(file_id=file_id, file_ext=".pdf")
        with open(file_dest, "w+b") as result_file_target:
            pisa.CreatePDF(
                html,
                result_file_target
            )
        
        print(f'temp_files_dir: {os.listdir(temp_files_dir)}')

        os.chmod(file_dest, 0o644)
        
        return file_id

    def create_file_name(self, template_path: str):
        return f"{template_path}.pdf"

    def create_pdf_file_response(self, file: BytesIO, filename: str):
        response = HttpResponse(content_type="application/pdf", content=file.getvalue())
        response["Content-Disposition"] = f'attachment; filename="{filename}.pdf"'

        return response
