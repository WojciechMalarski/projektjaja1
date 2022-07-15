import math

import django.utils.timezone
from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone
# Create your models here.

Kurnik_Choices = (
    ('Kurnik K1',"Kurnik K1"),
    ('Kurnik K3',"Kurnik K3"),
)
class KurnikProdukcja(models.Model):

    Kurnik = models.CharField(max_length=10,choices=Kurnik_Choices,default="Kurnik K3")
    IloscSS = models.FloatField(default=0)
    IloscS = models.FloatField(default=0)
    Ilosc1A = models.FloatField(default=0)
    Ilosc1B = models.FloatField(default=0)
    Ilosc2A = models.FloatField(default=0)
    Ilosc2B = models.FloatField(default=0)
    Stloczki = models.FloatField(default=0)
    Dataprodukcji = models.DateField(default=django.utils.timezone.now)
    Sumaprodukcji= models.FloatField(default=0)


    def save(self, *args, **kwargs):

        self.Sumaprodukcji = self.IloscSS + self.IloscS +self.Ilosc1A + self.Ilosc1B +self.Ilosc2A + self.Ilosc2B
        dec,whole = math.modf(self.Sumaprodukcji)
        if dec<0.12:
            whole = whole
            dec1 = dec
        if dec>=0.12 and dec <0.24:
            whole = whole+1
            dec1 = dec%0.12
        elif dec>=0.24 and dec <0.36:
            whole = whole+2
            dec1 = dec%0.12
        elif dec>=0.36 and dec <0.48:
            whole = whole+3
            dec1 = dec%0.12
        elif dec>=0.48 and dec <0.60:
            whole = whole+4
            dec1 = dec%0.12
        self.Sumaprodukcji = whole+dec1
        self.Sumaprodukcji= round( self.Sumaprodukcji,2)
        super(KurnikProdukcja, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}".format(self.Sumaprodukcji)
class Uwagi(models.Model):
    kurnik = models.CharField(max_length=10,choices=Kurnik_Choices,default="Kurnik K3")
    Uwagi = models.CharField(max_length=300,blank=True)
    upadki = models.IntegerField(default=0)
    data = models.DateField(default=django.utils.timezone.now)
    def __str__(self):
        return "{0}".format(self.upadki)
class Klient(models.Model):
    Imie = models.CharField(max_length=300)
    Nazwisko = models.CharField(max_length=300)
    Data = models.DateField(default=django.utils.timezone.now)
    def __str__(self):
        return "{0} {1}".format(self.Imie,self.Nazwisko)
class Suma(models.Model):
    klient=models.ForeignKey(Klient,on_delete=models.CASCADE,blank=True, null=True)
    IloscSS = models.IntegerField(default=0)
    CenaSS = models.IntegerField(default=200)
    SumaSS = models.IntegerField(default=0)
    IloscS = models.IntegerField(default=0)
    CenaS = models.IntegerField(default=190)
    SumaS = models.IntegerField(default=0)
    Ilosc1A = models.IntegerField(default=0)
    Cena1A = models.IntegerField(default=160)
    Suma1A = models.IntegerField(default=0)
    Ilosc1B = models.IntegerField(default=0)
    Cena1B = models.IntegerField(default=130)
    Suma1B = models.IntegerField(default=0)
    Ilosc2A = models.IntegerField(default=0)
    Cena2A = models.IntegerField(default=110)
    Suma2A = models.IntegerField(default=0)
    Sumaogolna = models.IntegerField(default=0)
    DataZamowienia = models.DateField(default=django.utils.timezone.now)
    def save(self, *args, **kwargs):
        self.SumaSS = self.IloscSS * self.CenaSS
        super(Suma, self).save(*args, **kwargs)
        self.SumaS = self.IloscS * self.CenaS
        super(Suma, self).save(*args, **kwargs)
        self.Suma1A = self.Ilosc1A * self.Cena1A
        super(Suma, self).save(*args, **kwargs)
        self.Suma1B = self.Ilosc1B * self.Cena1B
        super(Suma, self).save(*args, **kwargs)
        self.Suma2A = self.Ilosc2A * self.Cena2A
        super(Suma, self).save(*args, **kwargs)
        self.Sumaogolna = self.SumaSS + self.SumaS+self.Suma1A + self.Suma1B+self.Suma2A
        super(Suma, self).save(*args, **kwargs)
    def __str__(self):
        return "{0}".format(self.Sumaogolna)
    def get_absolute_url(self):
        return reverse('zamowienie_detail', args=(str(self.pk)))
