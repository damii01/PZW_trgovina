import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Kupac, VrstaProizvoda, Adress, Proizvod
from main.factory import (
    KupacFactory,
    AdressFactory,
    ProizvodFactory,
    VrstaProizvodaFactory,
)

NUM_KUPAC = 100
NUM_ADDRESS = 200
NUM_PROIZVOD = 150
NUM_VRSTA_PROZVODA = 5
PROIZVODS_PER_KUPAC = 3


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Proizvod, VrstaProizvoda, Adress, Kupac]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        proizvodi = []
            
        for _ in range(NUM_VRSTA_PROZVODA):
            vrsta_proizvoda = VrstaProizvodaFactory()
            
        for _ in range(NUM_PROIZVOD):
            proizvod = ProizvodFactory()
            proizvodi.append(proizvod)
            
        for _ in range(NUM_ADDRESS):
            adress = AdressFactory()
            
        for _ in range(NUM_KUPAC):
            kupac = KupacFactory()
            ran = random.choices(
                proizvodi,
                k = 2
            )
            kupac.kupac_proizvodi.add(*ran)
            print(*ran)
            print("")

