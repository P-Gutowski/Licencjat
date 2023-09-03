from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Post, Kategoria


class UserRegistrationTest(TestCase):
    def test_register_new_user(self):
        user_data = {
            'username': 'newuser',
            'first_name': 'newuser',
            'surname': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Pass123!!!',
            'password2': 'Pass123!!!'
        }
        
        response = self.client.post(reverse('register'), data=user_data)
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

class PostCreationTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='superuser', password='superpass', email='superuser@example.com',)
        self.client.login(username='superuser', password='superpass')
        self.kategoria = Kategoria.objects.create(tytul_kat="Test Kategoria", opis="<p>Opis testowej kategorii.</p>", obraz='media/posty/112df9fa395ca421b77ba0e2951df28a7f1afb04e50c653df060c3950f530130.jpg')

    def test_superuser_can_create_post(self):
        url = reverse('dodaj_post') 
        post_data = {
            'tytul_post': 'Tytuł testowego postu',
            'tekst': '<p>Treść testowego postu.</p>',
            'obraz': 'media/posty/112df9fa395ca421b77ba0e2951df28a7f1afb04e50c653df060c3950f530130.jpg',
            'kategoria': self.kategoria.id_kat
        }

        response = self.client.post(url, data=post_data)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(Post.objects.count(), 0)  

class CategoryCreationTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='superuser', password='superpass', email='superuser@example.com',)
        self.client.login(username='superuser', password='superpass')

    def test_superuser_can_create_post(self):
        url = reverse('dodaj_kategorie') 
        post_data = {
            'tytul_kat': 'Tytuł ',
            'opis': '<p>Treść</p>',
            'obraz': 'media/posty/112df9fa395ca421b77ba0e2951df28a7f1afb04e50c653df060c3950f530130.jpg'
        }

        response = self.client.post(url, data=post_data)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(Kategoria.objects.count(), 0)  


class GroupCreationTest(TestCase):
    
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username='superuser',
            password='superuserpassword',
            email='superuser@example.com'
        )
        self.client.force_login(self.superuser)
    
    def test_superuser_can_create_group(self):
        group_name = "Test Group"
        response = self.client.post('/admin/auth/group/add/', {
            'name': group_name, 
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Group.objects.filter(name=group_name).exists())
