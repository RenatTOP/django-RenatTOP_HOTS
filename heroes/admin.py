from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from heroes.models import Hero


class HeroAdmin(TabbedTranslationAdmin):
    list_display = ("title", "title_min", "hero_type")
    list_filter = ['hero_type']
    search_field = ('title')
    ordering = ['title']


admin.site.register(Hero, HeroAdmin)
