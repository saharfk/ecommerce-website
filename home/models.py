from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comments(models.Model):

    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.CharField(blank=True, max_length=30)
    commentInfo = models.TextField(blank=True, max_length=90)

    def __str__(self):
        return self.service
