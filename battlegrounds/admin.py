from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from battlegrounds.models import Battleground


class BattlegroundAdmin(TabbedTranslationAdmin):
    list_display = ("title", "title_min1", "title_min2", "title_min3")
    search_field = ('title')
    ordering = ['title']


admin.site.register(Battleground, BattlegroundAdmin)
