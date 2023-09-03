"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
import django.contrib.auth.urls
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.http import HttpResponseRedirect
from .views import LikeView, add_comment, home, PostView, add_post, update_post, usun_post, add_category, KategoriaView, update_kategorie, usun_kategorie, kontakt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('dodaj_post/', add_post.as_view(), name='dodaj_post'),
    path('dodaj_kategorie/', add_category.as_view(), name='dodaj_kategorie'),
    path('artykul/<int:pk>/edytuj', update_post.as_view(), name='update_post'),
    path('artykul/<int:pk>/usun', usun_post.as_view(), name='usun_post'),
    path('kategoria/<int:pk>/edytuj', update_kategorie.as_view(), name='update_cat'),
    path('kategoria/<int:pk>/usun', usun_kategorie.as_view(), name='usun_cat'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', home),
    path('kontakt/', kontakt),
    path('uzytkownicy/', include('django.contrib.auth.urls')),
    path('uzytkownicy/', include('uzytkownicy.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('artykul/<int:pk>', PostView.as_view(), name='post'),
    path('kategoria/<slug:id_kat>', KategoriaView, name='kategoria'),
    path('lajkuj/<int:pk>', LikeView, name='lajkuj'),
    path('add_comment/<int:id_post>', add_comment.as_view(), name='add_comment',)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
