from distutils.text_file import TextFile
from django.db import models
from django.forms import CharField

# Create your models here.
# Jedna klassa w tym pliku odpowiada jednej tabeli w bazie

class Producent(models.Model):
    
    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa
    
    class Meta:
        verbose_name ="Producent"             # nazwya baze danych po naszemu dla liczby pojedynczej
        verbose_name_plural = "Producenci"  

class Kategoria(models.Model):
    
    nazwa = models.CharField(max_length=60)

    def __str__(self):
        return self.nazwa
    
    class Meta:
        verbose_name ="Kategoria"             # nazwya baze danych po naszemu dla liczby pojedynczej
        verbose_name_plural = "Kategorie"


class Produkty(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    obrazek = models.ImageField(upload_to ='uploads/',height_field=None, width_field=None,blank=True,null=True)

    producent = models.ForeignKey(Producent,on_delete=models.CASCADE,null=True,blank=True) # określamy relacje pomiędzy tabelami w bazie danych 
    kategoria = models.ForeignKey(Kategoria,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):          # wyświetla się po nazwie w panelu admin
        return self.nazwa
    
    class Meta:
        verbose_name ="Produkt"             # nazwya baze danych po naszemu dla liczby pojedynczej
        verbose_name_plural = "Produkty"    # dla liczby mnogiej
