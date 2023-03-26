from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store, Tub

# Create your views here.
def homePage(request):
    #return HttpResponse("Hello, World!")
    return render(request, "IceCreamApp/homePageBase.html") 

def listOfTubs(request):
    tubs = Tub.objects.all()
    return render(request, "IceCreamApp/listOfTubs.html", {"tubs": tubs})

def listOfStores(request):
    stores = Store.objects.all()
    return render(request, "IceCreamApp/listOFStores.html", {"stores": stores}) 

def viewSingleStore(request, store_id):
    myStore = get_object_or_404(Store, id = store_id) # get single store by id
    tubobjects = Tub.objects.filter(store = myStore) # get store tubs
    tot_size = 0 # get total tub size
    for i in tubobjects:
        tot_size += i.size

    return render(request, "IceCreamApp/store.html", {"store": myStore, "storeTubs" : tubobjects, "totalSize" : tot_size}) 