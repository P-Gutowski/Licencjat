from django.contrib import admin
from .models import Kategoria, Post, Komentarz
# Register your models here.
#Konfiguracja admina

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('tag_obraz','tytul_kat', 'opis', 'url', 'kiedy_dodane')
    search_fields = ('tytul_kat',)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tag_obraz','tytul_post', 'tekst', 'url', 'kiedy_dodane')
    search_fields = ('tytul_kat',)
    list_filter = ('kategoria',)
    list_per_page = 50



admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Komentarz)

