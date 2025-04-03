from ipaddress import ip_address
from typing import Optional
from django.http import HttpRequest, HttpResponse
from main.models import RequestLog
from main.repositories.base import BaseRepository


class RequestLogRepository(BaseRepository):
    def create_request_log(self, request: HttpRequest, response: HttpResponse) -> RequestLog:
        return RequestLog.objects.create(
            http_method=request.method,
            path=request.path,
            query=request.get_full_path_info().split('/')[-1],
            ip_address=request.META["REMOTE_ADDR"],
            status=response.status_code
        )
        
    async def get_request_list(self, page: int = 1, per_page: int = 10) -> list[RequestLog]:
        data = []
        async for log in RequestLog.objects.all()[(page - 1) * per_page : per_page].aiterator():
            data.append(log)
        return data
