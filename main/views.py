from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.views.generic import ListView

## Create your views here.
def homepage(request):
    return render(request, 'homepage.html')



def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>Trenutno vrijeme: {}. <br> <a href="/">Vrati se na početnu</a></body></html>'.format(now)
    return HttpResponse(html)

def all_kupac(request):
    kupci = Kupac.objects.all()
    
    context = {'kupci':kupci}
    
    return render(request, 'all_kupac.html', context=context)


class KupacList(ListView):
    model = Kupac
    

class AdressList(ListView):
    model = Adress
    
class VrstaProizvodaList(ListView):
    model = VrstaProizvoda
    
class ProizvodList(ListView):
    model = Proizvod