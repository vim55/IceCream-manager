from django.shortcuts import render, get_object_or_404
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
    myStore = get_object_or_404(Store, id = store_id)
    tubobjects = Tub.objects.filter(store = myStore)

    return render(request, "IceCreamApp/store.html", {"store": myStore, "storeTubs" : tubobjects}) 