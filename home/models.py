from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField( upload_to="images/", null=True, blank=True, verbose_name='Картинка')
    users = models.ManyToManyField(User, related_name='Avatar_images')

    def __str__(self):
        return self.title
