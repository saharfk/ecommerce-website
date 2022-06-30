from django.db import models


# from django.contrib.auth.models import User


# Create your models here.
class CV(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(blank=True, max_length=120)
    image = models.ImageField(blank=True, upload_to='images/')
    Info = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title


class Website(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(blank=True, max_length=120)
    URL = models.CharField(blank=True,  max_length=120)
    Info = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title


class Python(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(blank=True, max_length=120)
    image = models.ImageField(blank=True, upload_to='images/')
    Info = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title


class Others(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(blank=True, max_length=120)
    image = models.ImageField(blank=True, upload_to='images/')
    Info = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title

# image = models.ImageField(upload_to='images/', null=False)
