from django.contrib import admin
from.models import *

# Register your models here.
model_list = [Kupac, VrstaProizvoda, Adress, Proizvod]

admin.site.register(model_list)