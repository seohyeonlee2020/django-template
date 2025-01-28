from django.shortcuts import render
from django.http import HttpResponse


def viewname(request):
    return HttpResponse("Hello, world. first view here.")
