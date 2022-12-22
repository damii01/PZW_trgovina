## factories.py
import factory
from factory.django import DjangoModelFactory
from main.models import *

## Defining a factory

class AdressFactory(DjangoModelFactory):
    class Meta:
        model = Adress

    adress_country = factory.Faker("country")
    adress_city = factory.Faker("city")
    adress_name = factory.Faker("street_name")
    adress_number = factory.Faker("building_number")
    
    
class VrstaProizvodaFactory(DjangoModelFactory):
    class Meta:
        model = VrstaProizvoda

    vrstaP_naziv = factory.Faker("name")


class ProizvodFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod

    proizvod_brand = factory.Faker("company")
    proizvod_size = factory.Faker("random_uppercase_letter")
    proizvod_color = factory.Faker("color_name")
    proizvod_naziv = factory.Faker("name")
    proizvod_price = factory.Faker("pyfloat", min_value = 10, max_value = 900)
    proizvod_discount = factory.Faker("pyint", min_value = 0, max_value = 70)
    proizvod_slika = factory.Faker("image_url")
    proizvod_vrstaP = factory.Iterator(VrstaProizvoda.objects.all())

class KupacFactory(DjangoModelFactory):
    class Meta:
        model = Kupac

    kupac_ime = factory.Faker("first_name")
    kupac_prezime = factory.Faker("last_name")
    kupac_email = factory.Faker("email")
    kupac_placanje =factory.Faker("name")
    kupac_adresa = factory.Iterator(Adress.objects.all())