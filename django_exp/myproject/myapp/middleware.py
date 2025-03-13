import datetime
import time
from django.utils.timezone import now

class ActivityLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        url = request.path
        timestamp = now()
        print(f"[{timestamp}] User: {user} accessed {url}")
        response = self.get_response(request)
        return response
    
class ExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        execution_time = end_time-start_time
        print(f"Execution Time: {execution_time:.5f} seconds")
        return response