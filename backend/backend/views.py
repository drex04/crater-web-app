rom django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome to the Crater Homepage.")