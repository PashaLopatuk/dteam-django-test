from django.http.request import HttpRequest
from pprint import pprint

from main.repositories.request_log import RequestLogRepository


class RequestLogMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        self._request_log_repo = RequestLogRepository()
    
    def __call__(self, request: HttpRequest):
        
        response = self._get_response(request)
        
        self._request_log_repo.create_request_log(request=request, response=response)

        return response
