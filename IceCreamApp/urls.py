from django.urls import path
from .views import homePage, listOfTubs, listOfStores, viewSingleStore

urlpatterns = [
    path("", homePage, name="homePage"),
    path("tubs/", listOfTubs, name="tubs"),
    path("stores/", listOfStores, name="stores"),
    path("stores/<int:store_id>", viewSingleStore, name="store"),
]