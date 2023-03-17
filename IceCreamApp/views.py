from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Store, Tub

# Create your views here.
def homePage(request):
    #return HttpResponse("Hello, World!")
    return render(request, "IceCreamApp/homePageBase.html") 

def listOfTubs(request):
    tubs = Tub.objects.all()
    return render(request, "IceCreamApp/listOFTubs.html", {"tubs": tubs}) 

def listOfStores(request):
    stores = Store.objects.all()
    return render(request, "IceCreamApp/listOFStores.html", {"stores": stores}) 

def viewSingleStore(request, store_id):
    #stores = Store.objects.all()
    store = Store.objects.get(id = store_id)
    print(store)
    #return render(request, "IceCreamApp/store.html", {"store": stores}) 
    #return HttpResponse(store_id)
    return render(request, "IceCreamApp/store.html", {"store": store}) 