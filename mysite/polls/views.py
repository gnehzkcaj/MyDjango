from django.http import HttpResponse
from django.utils import timezone

def index(request):
    current_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    response_text = f"Hello, world. You're at the polls index. Current time is: {current_time}"
    return HttpResponse(response_text)
