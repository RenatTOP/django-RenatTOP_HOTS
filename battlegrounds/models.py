from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User

class Battleground(models.Model):
    title =  models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    preview_url = models.CharField(max_length=1024)
    url = models.CharField(max_length=50, default='')
    title_min1 = models.CharField(max_length=50)
    title_min2 = models.CharField(max_length=50)
    title_min3 = models.CharField(max_length=50)
    desc1 =  models.CharField(max_length=200)
    desc2 =  models.CharField(max_length=200)
    desc3 =  models.CharField(max_length=200)
    pictures_url = JSONField(default=dict)
    big_pictures_url = JSONField(default=dict)
    users = models.ManyToManyField(User, related_name='favorite_bg')

    def __str__(self):
        return self.title
