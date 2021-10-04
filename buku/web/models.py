from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    nama = models.CharField(max_length=25)

    def __str__(self):
        return self.nama

class Post(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    thumb = models.ImageField(upload_to = "images/",blank=True, null=True)
    deskripsi = models.TextField(max_length=255)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False)
    slug = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.title

    def save(self):
        self.slug =slugify(self.title)
        super().save()

