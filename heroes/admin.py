from heroes.models import Hero
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin


class HeroAdmin(TabbedTranslationAdmin):
    list_display = ("title", "title_min", "hero_type")
    list_filter = ['hero_type']
    search_field = ('title')
    ordering = ['title']


admin.site.register(Hero, HeroAdmin)
