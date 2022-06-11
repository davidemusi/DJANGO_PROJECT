from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Zuri Team. Welcome to my Django app.")