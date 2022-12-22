from django.db import models

# Create your models here.

class VrstaProizvoda(models.Model):
    vrstaP_naziv = models.CharField(max_length=50)
    
    def __str__(self):
        return self.vrstaP_naziv
    
    
class Proizvod(models.Model):
    proizvod_brand = models.CharField(max_length=100)
    proizvod_size = models.CharField(max_length=4)
    proizvod_color = models.CharField(max_length=15)
    proizvod_naziv = models.CharField(max_length=70)
    proizvod_price = models.FloatField()
    proizvod_discount = models.FloatField()
    proizvod_slika = models.URLField()
    proizvod_vrstaP = models.ForeignKey(VrstaProizvoda, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.proizvod_naziv +" " + self.proizvod_brand +" " + str(self.proizvod_price) +" "+ str(self.proizvod_vrstaP)
    
    
class Adress(models.Model):
    adress_country = models.CharField(max_length=30)
    adress_city = models.CharField(max_length=80)
    adress_name = models.CharField(max_length=100)
    adress_number = models.CharField(max_length=4)
    def __str__(self):
        return self.adress_city + ", "+ self.adress_name + " " + self.adress_number
    
class Kupac(models.Model):
    kupac_ime = models.CharField(max_length=100)
    kupac_prezime = models.CharField(max_length=100)
    kupac_email = models.EmailField()
    kupac_placanje = models.CharField(max_length=50)
    kupac_proizvodi = models.ManyToManyField(Proizvod)
    kupac_adresa = models.OneToOneField(
        Adress,
        on_delete=models.CASCADE,
    )
      
    def __str__(self):
        return self.kupac_ime


    
    
    
    
