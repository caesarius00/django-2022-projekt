from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *
from .formularz import *
# Create your views here.

def index(request):
    return render(request,'index.html')
    
def adres(request):
    things = Adres.objects.all()
    ile = len(things)
    form = AdresForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'adres.html', {'baza': things, 'ilosc': ile, 'form':form})

def adresEdit(request, id):
    edit = get_object_or_404(Adres, pk=id)
    form = AdresForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def adresDelete(request, id):
    usun = get_object_or_404(Adres, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def klient(request):
    things = Klient.objects.all()
    ile = len(things)
    form = KlientForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'klient.html', {'baza': things, 'ilosc': ile, 'form':form})

def klientEdit(request, id):
    edit = get_object_or_404(Klient, pk=id)
    form = KlientForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def klientDelete(request, id):
    usun = get_object_or_404(Klient, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def krawiec(request):
    things = Krawiec.objects.all()
    ile = len(things)
    form = KrawiecForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'krawiec.html', {'baza': things, 'ilosc': ile, 'form':form})

def krawiecEdit(request, id):
    edit = get_object_or_404(Krawiec, pk=id)
    form = KrawiecForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def krawiecDelete(request, id):
    usun = get_object_or_404(Krawiec, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def opinia(request):
    things = Opinia.objects.all()
    ile = len(things)
    form = OpiniaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'opinia.html', {'baza': things, 'ilosc': ile, 'form':form})

def opiniaEdit(request, id):
    edit = get_object_or_404(Opinia, pk=id)
    form = OpiniaForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def opiniaDelete(request, id):
    usun = get_object_or_404(Opinia, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def personalizowany_towar(request):
    things = PersonalizowanyTowar.objects.all()
    ile = len(things)
    form = personalizowany_towarForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'personalizowany_towar.html', {'baza': things, 'ilosc': ile, 'form':form})

def personalizowany_towarEdit(request, id):
    edit = get_object_or_404(PersonalizowanyTowar, pk=id)
    form = personalizowany_towarForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def personalizowany_towarDelete(request, id):
    usun = get_object_or_404(PersonalizowanyTowar, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def towar(request):
    things = Towar.objects.all()
    ile = len(things)
    form = TowarForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'towar.html', {'baza': things, 'ilosc': ile, 'form':form})

def towarEdit(request, id):
    edit = get_object_or_404(Towar, pk=id)
    form = TowarForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def towarDelete(request, id):
    usun = get_object_or_404(Towar, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def zamowienie(request):
    things = Zamowienie.objects.all()
    ile = len(things)
    form = ZamowienieForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'zamowienie.html', {'baza': things, 'ilosc': ile, 'form':form})

def zamowienieEdit(request, id):
    edit = get_object_or_404(Zamowienie, pk=id)
    form = ZamowienieForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def zamowienieDelete(request, id):
    usun = get_object_or_404(Zamowienie, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

def zwrot(request):
    things = Zwrot.objects.all()
    ile = len(things)
    form = ZwrotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'zwrot.html', {'baza': things, 'ilosc': ile, 'form':form})

def zwrotEdit(request, id):
    edit = get_object_or_404(Zwrot, pk=id)
    form = ZwrotForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
    return render(request, 'edit.html',{'form': form})

def zwrotDelete(request, id):
    usun = get_object_or_404(Zwrot, pk=id)
    if request.method == "POST":
        usun.delete()
    return render(request, 'delete.html',{'usun': usun})

"""def dodajAdres(request):
    form = AdresForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render()"""