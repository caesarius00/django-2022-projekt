from operator import truediv
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Zwrot(models.Model):
    idZwrot = models.IntegerField(primary_key=True)
    Nick = models.ForeignKey("Klient", blank=True, null=True, on_delete=models.SET_NULL)
    Towar = models.ForeignKey("Towar", blank=True, null=True, on_delete=models.SET_NULL)
    Powod = models.CharField(max_length=256)
    dataWyslania = models.DateField()
    dataOtrzymania = models.DateField(null=True, blank=True)
    czyZwroconoPieniadze = models.BooleanField()

    def __str__(self):
        return self.all()

    def all(self):
        #return "|{}|: {}; {}; {}; {}; {}".format(self.idZwrot, self.Nick, self.Powod, self.dataWyslania, self.dataOtrzymania, self.czyZwroconoPieniadze)    
        return format_html("Nr: {}, {}, <br/>Powód: {}",self.idZwrot, self.Nick, self.Powod)

class Klient(models.Model):
    Nick = models.CharField(primary_key=True,max_length=20)
    idAdres = models.ForeignKey("Adres", blank=True, on_delete=models.SET_NULL, null=True)
    Imie = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    nrTelefonu = models.CharField(max_length=9)
    Email = models.CharField(max_length=30)

    def __str__(self):
        return self.all()

    def all(self):
        #return "|{}|: {}; {}; {}; {}; {}".format(self.Nick, self.idAdres, self.Imie, self.Nazwisko, self.nrTelefonu, self.Email)
        return "{}, {}".format(self.Nick, self.Email)

class Opinia(models.Model):
    idOpinia = models.IntegerField(primary_key=True)
    Nick = models.ForeignKey("Klient", null=True, blank=True, on_delete=models.SET_NULL)
    idTowar = models.ForeignKey("Towar", null=True, blank=True, on_delete=models.SET_NULL)
    Gwiazdki = models.IntegerField()
    Komentarz = models.CharField(max_length=256)

    def __str__(self):
        return self.all()

    def all(self):
        return "{}: ({}/5) {}".format(self.Nick.Nick, self.Gwiazdki, self.Komentarz)

class Towar(models.Model):
    idTowar = models.IntegerField(primary_key=True)
    idKrawiec = models.ForeignKey("Krawiec", blank=True, on_delete=models.CASCADE)
    Nazwa = models.CharField(max_length=50)
    Material = models.CharField(max_length=20)
    Cena = models.IntegerField()

    def __str__(self):
        return self.all()

    def all(self):
        #return "|{}|: {}; {}; {}; {}".format(self.idTowar, self.idKrawiec, self.Nazwa, self.Material, self.Cena)
        return format_html("Towar: {}, <br/>Materiał: {},<br/>Cena: {}zł.", self.Nazwa, self.Material, self.Cena)


class PersonalizowanyTowar(models.Model):
    idPersonalizowany = models.IntegerField(primary_key=True)
    #idZwrot = models.ForeignKey("Zwrot", blank=True, on_delete=models.SET_NULL, null=True)
    idTowar = models.ForeignKey("Towar", blank=True, on_delete=models.CASCADE)
    idZamowienie = models.ForeignKey("Zamowienie", blank=True, on_delete=models.CASCADE)
    Rozmiar = models.CharField(max_length=6)
    Kolor = models.CharField(max_length=20)
    czyWyprodukowano = models.BooleanField()

    def __str__(self):
        return self.all()

    def all(self):
        return "{}, rozmiar: {}, kolor: {}, z zamówienia {}".format(self.idTowar.Nazwa, self.Rozmiar, self.Kolor, self.idZamowienie.idZamowienie)

class Zamowienie(models.Model):
    idZamowienie = models.IntegerField(primary_key=True)
    Nick = models.ForeignKey("Klient", null=True, blank=True, on_delete=models.SET_NULL)
    sposobPlatnosci = models.CharField(max_length=30, null=True)
    dataZamowienia = models.DateField()
    dataWyslania = models.DateField(null=True, blank=True)
    dataDostarczenia = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.all()

    def all(self):
        #return "|{}|: {}; {}; {}; {}; {}".format(self.idZamowienie, self.Nick, self.sposobPlatnosci, self.dataZamowienia, self.dataWyslania, self.dataDostarczenia)
        return "Nr: {}, {}".format(self.idZamowienie, self.Nick)
    
class Adres(models.Model):
    idAdres = models.IntegerField(primary_key=True)
    kodPocztowy = models.CharField(max_length=6)
    Miasto = models.CharField(max_length=30)
    Ulica = models.CharField(max_length=20)
    nrDomu = models.CharField(max_length=10)

    def __str__(self):
        return self.all()

    def all(self):
        #return "|{}|: {}; {}; {}; {}".format(self.idAdres, self.kodPocztowy, self.Miasto, self.Ulica, self.nrDomu)
        return "{} {}, ul. {} {}".format(self.kodPocztowy, self.Miasto, self.Ulica, self.nrDomu)

class Krawiec(models.Model):
    idKrawiec = models.IntegerField(primary_key=True)
    idAdres = models.ForeignKey("Adres", blank=True, null=True, on_delete=models.SET_NULL)
    Imie = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    nrTelefonu = models.CharField(max_length=9)
    Email = models.CharField(max_length=30)

    def __str__(self):
        return self.all()

    def all(self):
        return "{} {}, tel. {}, {}".format(self.Imie, self.Nazwisko, self.nrTelefonu, self.Email)