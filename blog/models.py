from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=250)
    text = models.TextField(("Content"))

    created_date = models.DateTimeField(('Created Date'), auto_now_add=True)
    published_date = models.DateTimeField(("Published Date"), auto_now=True)


    def __str__(self):
        return "{}".format(self.title)

# Create your models here.
