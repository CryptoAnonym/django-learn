from django.contrib import admin
from .models import Kategoria, Producent, Produkty

# Register your models here.
admin.site.register(Produkty)  # rejstrujemy w panelu admina tabele utworzone w models
admin.site.register(Producent)
admin.site.register(Kategoria)