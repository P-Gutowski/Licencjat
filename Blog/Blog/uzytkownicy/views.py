from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.forms import NewUserForm, EditUserForm

class UzytkownikRejestracja(generic.CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class Uzytkownik_edycja(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edytuj_profil.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user


