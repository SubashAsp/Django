from django.http import HttpResponse # type: ignore

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index")
