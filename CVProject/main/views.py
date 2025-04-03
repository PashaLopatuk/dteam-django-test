from typing import Callable
from django.core.handlers.base import sync_to_async
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import View
from reportlab.lib.pagesizes import C0

from main.repositories.cv import CvRepository
from main.repositories.request_log import RequestLogRepository
from utils.pdf import DjangoPdfResolver


class CVListView(View):
    def __init__(self):
        self._cv_repo = CvRepository()

    async def get(self, request: HttpRequest):
        cv_list = await self._cv_repo.get_all_cv()

        template_data = {"cv_list": cv_list}

        return render(
            request=request, template_name="cv_list.html", context=template_data
        )


class CVInfoView(View):
    def __init__(self):
        self._cv_repo = CvRepository()

    async def get(self, request: HttpRequest, cv_id: int):
        cv_data = await self._cv_repo.get_cv_by_id(id=cv_id)

        template_data = {"cv_data": cv_data}

        return render(
            request=request, template_name="cv_info.html", context=template_data
        )


class CVInfoPdfView(View):
    def __init__(self):
        self._cv_repo = CvRepository()
        self._pdf_resolver = DjangoPdfResolver()

    async def get(self, request: HttpRequest, cv_id: int):
        cv_data = await self._cv_repo.get_cv_by_id(id=cv_id)

        pdf_file = await self._pdf_resolver.render_pdf(
            request=request,
            template_path="cv_info_pdf.html",
            template_context={"cv_data": cv_data},
        )

        response = self._pdf_resolver.create_pdf_file_response(
            file=pdf_file, filename=str(cv_data)
        )

        return response


class RequestLogListView(View):
    def __init__(self):
        self._logs_repo = RequestLogRepository()
    
    async def get(self, request: HttpRequest):
        logs = await self._logs_repo.get_request_list(page=1, per_page=10)
        print(logs)
        return render(
            request=request,
            template_name='logs_list.html',
            context={
                "logs_data": logs
            }
        )


class SettingsPageView(View):
    async def get(self, request: HttpRequest):
        return render(request=request, template_name='settings.html')
