from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) :
        return str(self.category)

class Title(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) :
        return str(self.title)

class Blog(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.ForeignKey(Title,  on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, blank=True, null=True)
    Desc =  HTMLField(blank=True, null=True)
    keyword = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='static', null=True,blank=True)
    date = models.DateField( auto_now=True)

    def __str__(self) :
        return str(self.id)
