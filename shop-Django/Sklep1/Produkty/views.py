from django.forms import ImageField
from django.shortcuts import render
from .models import Produkty, Kategoria
 

# Create your views here.

def index(request):
    wszystkie = Produkty.objects.all() # .all wyszykje wszystkie obiekty z bazy
    jeden = Produkty.objects.get(pk=1) # .get uddajke się do konkretnego w bazie o danym id (pk)
    kat = Produkty.objects.filter(kategoria=2) # filtrujemy np po kategorii
    producent = Produkty.objects.filter(producent=1)
    kat_name = Kategoria.objects.get(pk=1)
    kategorie = Kategoria.objects.all()
    null = Produkty.objects.filter(kategoria__isnull=True) # dla pustych = true dla pełnych false kiedy chcemy wyswietlic 
    zawiera = Produkty.objects.filter(opis__icontains="karta") # zawiera w opisie slowo karta
    dane = {'kategorie' : kategorie}
    return render(request,"szablon.html", dane)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,"kategoria_produkt" : kategoria_produkt, 'kategorie' : kategorie }  
    return render(request, "kategoria_produkt.html", dane)

def new_func():
    kategorie = Kategoria.objects.all()
    return kategorie

def produkty(request, id):
    kategorie = Kategoria.objects.all()
    produkt_user = Produkty.objects.get(pk=id) 
    dane = {'produkt_user' : produkt_user, 'kategorie' : kategorie }
    return render(request, "produkt.html", dane)





