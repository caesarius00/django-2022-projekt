"""wyklad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplikacja.views import * 


urlpatterns = [
    path('admin&123/', admin.site.urls),
    path('index/',index),
    path('adres/',adres),
    path('klient/',klient),
    path('krawiec/',krawiec),
    path('opinia/',opinia),
    path('personalizowany_towar/',personalizowany_towar),
    path('towar/',towar),
    path('zamowienie/',zamowienie),
    path('zwrot/',zwrot),
    
    path('edit/adres/<int:id>',adresEdit),
    path('edit/klient/<str:id>',klientEdit),
    path('edit/krawiec/<int:id>',krawiecEdit),
    path('edit/opinia/<int:id>',opiniaEdit),
    path('edit/personalizowany_towar/<int:id>',personalizowany_towarEdit),
    path('edit/towar/<int:id>',towarEdit),
    path('edit/zamowienie/<int:id>',zamowienieEdit),
    path('edit/zwrot/<int:id>',zwrotEdit),

    path('delete/adres/<str:id>',adresDelete),
    path('delete/klient/<str:id>',klientDelete),
    path('delete/krawiec/<int:id>',krawiecDelete),
    path('delete/opinia/<int:id>',opiniaDelete),
    path('delete/personalizowany_towar/<int:id>',personalizowany_towarDelete),
    path('delete/towar/<int:id>',towarDelete),
    path('delete/zamowienie/<int:id>',zamowienieDelete),
    path('delete/zwrot/<int:id>',zwrotDelete),
]
