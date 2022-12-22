from django.urls import path
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', homepage, name='homepage'),
    path('datum/', current_datetime, name='current_datetime'),
    path('all_kupac/', all_kupac, name='all_kupac'),
    path('kupci/', KupacList.as_view()),
    path('adrese/', AdressList.as_view()),
    path('vrstaProizvoda/', VrstaProizvodaList.as_view()),
    path('proizvodi/', ProizvodList.as_view())
]
