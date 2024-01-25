from django.shortcuts import render
from django.http import HttpResponse

# my_to_do_app/views.py
# Create your views here.
def index(request):
    return HttpResponse("my_to_do_app first page")
