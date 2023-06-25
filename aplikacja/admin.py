from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Klient)
admin.site.register(Zwrot)
admin.site.register(Adres)
admin.site.register(Zamowienie)
admin.site.register(Towar)
admin.site.register(PersonalizowanyTowar)
admin.site.register(Krawiec)
admin.site.register(Opinia)