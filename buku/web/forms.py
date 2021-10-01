from django.contrib.auth.models import User

from . import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

class postForm(ModelForm):
    class Meta:
        model = models.Post
        fields=(
            'title',
            'deskripsi',
            'categories',
            'thumb',

        )
        labels = {
            'title': 'Judul',
            'thumb':'Masukan Gambar'
        }

        widgets ={
            'title': forms.TextInput(
                attrs={
                    'class' :'form-control form-control-lg',
                    'placeholder':'isi judul',
                    'tittle':'Nama',
                }
            ),
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Isi Pesan'

                }
            ),
            'categories': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

        }

class CreateForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email' ,'password1', 'password2',)
