from typing import Callable
from django.core.handlers.base import sync_to_async
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views import View

from main.models import CV

class CVListApiView(View):
    async def fetch_all_cv(self) -> list[CV]:
        data = []
        async for cv in CV.objects.all().aiterator():
            data.append(cv)
        return data
    
    async def get(self, request: HttpRequest):
        cv_list = await self.fetch_all_cv()
    
        template_data = {
            "cv_list": cv_list
        }
    
        return render(
            request=request, 
            template_name='cv_list.html', 
            context=template_data
        )


class CVInfoApiView(View):
    async def fetch_cv_by_id(self, id: int) -> CV:
        cv = await sync_to_async(
            lambda : CV.objects.get(id=id)
        )()
        return cv
    
    async def get(self, request: HttpRequest, cv_id: int):
        cv_data = await self.fetch_cv_by_id(id=cv_id)
    
        template_data = {
            "cv_data": cv_data
        }

        return render(
            request=request, 
            template_name='cv_info.html', 
            context=template_data
        )
