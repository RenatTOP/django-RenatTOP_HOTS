from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User

class Hero(models.Model):
    title =  models.CharField(max_length=50)
    title_min = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    hero_type = models.CharField(max_length=20)
    points = JSONField(default=dict)
    ability1 = models.CharField(max_length=50)
    ab_desc1 = models.CharField(max_length=600)
    ability2 = models.CharField(max_length=50)
    ab_desc2 = models.CharField(max_length=600)
    ability3 = models.CharField(max_length=50)
    ab_desc3 = models.CharField(max_length=600)
    heroic1 = models.CharField(max_length=50)
    heroic_desc1 = models.CharField(max_length=600)
    heroic2 = models.CharField(max_length=50)
    heroic_desc2 = models.CharField(max_length=600)
    ab_trait = models.CharField(max_length=50)
    trait_desc = models.CharField(max_length=600)
    users = models.ManyToManyField(User, related_name='favorite_heroes')

    class Meta:
        verbose_name_plural = "heroes"

    def __str__(self):
        return self.title
