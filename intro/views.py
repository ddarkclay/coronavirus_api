from http.client import HTTPResponse

from django.shortcuts import render


def intro(request):
    return render(request, 'intro/index.html')
