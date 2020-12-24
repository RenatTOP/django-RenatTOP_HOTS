from home.models import Image
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Image, ImageAdmin)