from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import DodajNotatkeView, AktualizujNotatkeView, UsunNotatkeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dodaj_notatke/', DodajNotatkeView.as_view(), name='dodaj_notatke'),
    path('aktualizuj_notatke/<int:pk>/', AktualizujNotatkeView.as_view(), name='aktualizuj_notatke'),
    path('usun_notatke/<int:pk>/', UsunNotatkeView.as_view(), name='usun_notatke'),
    path('', RedirectView.as_view(url='/dodaj_notatke/')),
]