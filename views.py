from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse("index")


def login(reuqest):
    return redirect("/login")
