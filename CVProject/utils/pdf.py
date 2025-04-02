from io import BytesIO
from typing import Any, Optional

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


from xhtml2pdf import pisa


class DjangoPdfResolver:
    async def render_pdf(
        self,
        request: HttpRequest,
        template_path: str,
        template_context: dict[str, Any],
    ) -> BytesIO:
        result_file = BytesIO()

        template = get_template(template_path)
        html = template.render(template_context)

        pisa_status = pisa.pisaDocument(BytesIO(html.encode()), result_file)

        if pisa_status.err:
            return HttpResponse(f"We had some errors <pre>{html}</pre>")

        return result_file

    def create_file_name(self, template_path: str):
        return f"{template_path}.pdf"

    def create_pdf_file_response(self, file: BytesIO, filename: str):
        response = HttpResponse(content_type="application/pdf", content=file.getvalue())
        response["Content-Disposition"] = f'attachment; filename="{filename}.pdf"'

        return response
