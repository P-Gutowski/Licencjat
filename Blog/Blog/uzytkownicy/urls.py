from django.urls import path
from .views import UzytkownikRejestracja, Uzytkownik_edycja

urlpatterns = [
    path('register/', UzytkownikRejestracja.as_view(), name='register'),
    path('edytuj_profil', Uzytkownik_edycja.as_view(), name='edit_profile'),
]