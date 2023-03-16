from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *

# Create your views here.
def homePage(request):
    #return HttpResponse("Hello, World!")
    return render(request, "IceCreamApp/homePage.html") 

