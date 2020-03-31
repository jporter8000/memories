from django.db import models
from django.forms import ModelForm

# Create your models here.
class People(models.Model):
    email = models.EmailField(max_length=254)