from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.urls import reverse
from PIL import Image

# Model kategorii

class Kategoria(models.Model):
    id_kat = models.AutoField(primary_key=True)
    tytul_kat = models.CharField(max_length=80)
    opis = HTMLField()
    url = models.SlugField(max_length=80, unique=True, blank=True)
    obraz = models.ImageField(upload_to='kategoria/')
    kiedy_dodane = models.DateTimeField(auto_now_add=True, null=True)

    def tag_obraz(self):
        return format_html('<img src="../media/{}" style="width:50px; height:50px"/>'.format(self.obraz))
    def __str__(self) -> str:
        return self.tytul_kat

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_post = models.AutoField(primary_key=True)
    tytul_post = models.CharField(max_length=80)
    tekst = HTMLField()
    url = models.SlugField(max_length=80, unique=True, blank=True)
    obraz = models.ImageField(upload_to='posty/')
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    kiedy_dodane = models.DateTimeField(auto_now_add=True, null=True)
    lajki = models.ManyToManyField(User, related_name='posty')

    def get_absolute_url(self):
        return reverse('login', args=[str(self.id)])
    
    def lajki_total(self):
        return self.lajki.count()

    def tag_obraz(self):
        return format_html('<img src="../media/{}" style="width:50px; height:50px"/>'.format(self.obraz))
    
    def __str__(self) -> str:
        return self.tytul_post
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.obraz.path)
        if img.height > 400 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.obraz.path)

class Komentarz(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_komment = models.AutoField(primary_key=True)
    tekst = HTMLField()
    post = models.ForeignKey(Post, related_name="Komentarze" ,on_delete=models.CASCADE)
    kiedy_dodane = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return '%s - %s' % (self.post.tytul_post, self.autor)

@receiver(pre_save, sender=Post)
def generate_post_url(sender, instance, **kwargs):
    instance.url = slugify(instance.tytul_post)

@receiver(pre_save, sender=Kategoria)
def generate_kategoria_url(sender, instance, **kwargs):
    instance.url = slugify(instance.tytul_kat)
