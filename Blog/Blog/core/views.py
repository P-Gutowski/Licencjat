from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
import requests
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView
from .models import Post, Kategoria, Komentarz
from .forms import PostForm, EditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
# Create your views here.

def home(request):
  cat = Kategoria.objects.all()
  posts = Post.objects.all()
  data = {
    'posts' : posts,
    'cats' : cat
  }
  return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    lajki_total = post.lajki_total()
    return render(request, 'post.html', {'post' : post, 'lajki_total' : lajki_total})
class PostView(DetailView):
   model = Post
   template_name = 'post.html'

   def get_context_data(self, *args, **kwargs):
      kategorie = Kategoria.objects.all()
      context = super(PostView, self).get_context_data()
      stuff = get_object_or_404(Post, id_post=self.kwargs['pk'])
      total_likes = stuff.lajki_total()
      zlajkowane = False

      if stuff.lajki.filter(id=self.request.user.id).exists():
         zlajkowane = True
      
      context["total_likes"] = total_likes
      context["zlajkowane"] = zlajkowane
      return context

def kategoria(request, url):
    kategoria = Kategoria.objects.get(url=url)
    return render(request, 'kategoria.html', {'kategoria' : kategoria})
class add_post(CreateView):
   
   model = Post
   template_name = 'add_post.html'
   fields = ['tytul_post', 'tekst', 'obraz', 'kategoria']
   success_url = '/'

class update_post(UpdateView):
   model = Post
   template_name = 'update_post.html'
   fields = ['tytul_post', 'tekst', 'obraz', 'kategoria']
   success_url = '/'
class usun_post(DeleteView):
   model = Post
   template_name = 'delete_post.html'
   success_url = '/'

class add_category(CreateView):
   
   model = Kategoria
   template_name = 'add_category.html'
   fields = ['tytul_kat', 'opis', 'obraz']
   success_url = '/'

class update_kategorie(UpdateView):
   model = Kategoria
   template_name = 'update_cat.html'
   fields = ['tytul_kat', 'opis', 'obraz']
   success_url = '/'
class usun_kategorie(DeleteView):
   model = Kategoria
   template_name = 'delete_cat.html'
   success_url = '/'
def KategoriaView(request, id_kat):
   posty_kategorii = Post.objects.filter(kategoria=id_kat)
   return render(request, 'kategoria.html', {'kategoria': kategoria, 'posty_kategorii': posty_kategorii})

def LikeView(request, pk):
  post = get_object_or_404(Post, id_post=request.POST.get('id_post'))
  zlajkowane = False
  if post.lajki.filter(id=request.user.id).exists():
     post.lajki.remove(request.user)
     zlajkowane = False
  else:
     post.lajki.add(request.user)
     zlajkowane = True
  return HttpResponseRedirect(reverse('post', args=[str(pk)]))

class add_comment(LoginRequiredMixin, CreateView):
   
   model = Komentarz
   template_name = 'add_comment.html'
   fields = ['tekst']
   success_url = '/'

   def form_valid(self, form):
        form.instance.autor = self.request.user  # Ustawiamy zalogowanego użytkownika jako autora
        form.instance.post = get_object_or_404(Post, id_post=self.kwargs['id_post'])  # Ustawiamy post na podstawie przekazanego ID
        return super().form_valid(form)
   
def kontakt(request):
  return render(request, 'kontakt.html')

   