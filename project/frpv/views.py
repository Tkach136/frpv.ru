from django.shortcuts import render
from django.http import Http404, HttpResponse
from pprint import pformat


def index(request):
    content = request.headers.items()
    return HttpResponse(content)

def get_data(request):
    pass
