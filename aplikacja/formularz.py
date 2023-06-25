from django.forms import ModelForm
from .models import *

class AdresForm(ModelForm):
    class Meta:
        model = Adres
        fields = ['idAdres', 'kodPocztowy', 'Miasto', 'Ulica', 'nrDomu']

class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = ['Nick', 'idAdres', 'Imie', 'Nazwisko', 'nrTelefonu', 'Email']

class KrawiecForm(ModelForm):
    class Meta:
        model = Krawiec
        fields = ['idKrawiec', 'idAdres', 'Imie', 'Nazwisko', 'nrTelefonu', 'Email']

class OpiniaForm(ModelForm):
    class Meta:
        model = Opinia
        fields = ['idOpinia', 'Nick', 'idTowar', 'Gwiazdki', 'Komentarz']

class personalizowany_towarForm(ModelForm):
    class Meta:
        model = PersonalizowanyTowar
        fields = ['idPersonalizowany', 'idTowar', 'idZamowienie', 'Rozmiar', 'Kolor', 'czyWyprodukowano']

class TowarForm(ModelForm):
    class Meta:
        model = Towar
        fields = ['idTowar', 'idKrawiec', 'Nazwa', 'Material', 'Cena']

class ZamowienieForm(ModelForm):
    class Meta:
        model = Zamowienie
        fields = ['idZamowienie', 'Nick', 'sposobPlatnosci', 'dataZamowienia', 'dataWyslania', 'dataDostarczenia']

class ZwrotForm(ModelForm):
    class Meta:
        model = Zwrot
        fields = ['idZwrot', 'Nick', 'Towar', 'Powod', 'dataWyslania', 'dataOtrzymania', 'czyZwroconoPieniadze']