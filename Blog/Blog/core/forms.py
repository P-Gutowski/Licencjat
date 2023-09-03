from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post


# Create your forms here.

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "surname","email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tytul_post', 'tekst', 'obraz', 'kategoria']  # lub użyj fields = '__all__' aby uwzględnić wszystkie pola

    wigets = {
		'tytul_posta' : forms.TextInput(attrs={'class': 'form-control'}),
		'tekst' : forms.TextInput(attrs={'class': 'form-control'}),
		'obraz' : forms.TextInput(attrs={'class': 'form-control'}),
		'kategoria' : forms.TextInput(attrs={'class': 'form-control'})
    }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tytul_post', 'tekst', 'obraz', 'kategoria']  # lub użyj fields = '__all__' aby uwzględnić wszystkie pola

    wigets = {
		'tytul_posta' : forms.TextInput(attrs={'class': 'form-control'}),
		'tekst' : forms.TextInput(attrs={'class': 'form-control'}),
		'obraz' : forms.TextInput(attrs={'class': 'form-control'}),
		'kategoria' : forms.TextInput(attrs={'class': 'form-control'})
    }
class EditUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "surname","email")



