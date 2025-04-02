from typing import Callable
from django.core.handlers.base import sync_to_async
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import View

from main.repositories.cv import CvRepository
from utils.pdf import DjangoPdfResolver


class CVListApiView(View):
    def __init__(self):
        self._cv_repo = CvRepository()

    async def get(self, request: HttpRequest):
        cv_list = await self._cv_repo.fetch_all_cv()

        template_data = {"cv_list": cv_list}

        return render(
            request=request, template_name="cv_list.html", context=template_data
        )


class CVInfoApiView(View):
    def __init__(self):
        self._cv_repo = CvRepository()

    async def get(self, request: HttpRequest, cv_id: int):
        cv_data = await self._cv_repo.fetch_cv_by_id(id=cv_id)

        template_data = {"cv_data": cv_data}

        return render(
            request=request, template_name="cv_info.html", context=template_data
        )


class CVInfoPdfApiView(View):
    def __init__(self):
        self._cv_repo = CvRepository()
        self._pdf_resolver = DjangoPdfResolver()

    async def get(self, request: HttpRequest, cv_id: int):
        cv_data = await self._cv_repo.fetch_cv_by_id(id=cv_id)

        pdf_file = await self._pdf_resolver.render_pdf(
            request=request,
            template_path="cv_info_pdf.html",
            template_context={"cv_data": cv_data},
        )

        response = self._pdf_resolver.create_pdf_file_response(
            file=pdf_file, filename=str(cv_data)
        )

        return response
