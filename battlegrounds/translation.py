from modeltranslation.translator import translator, TranslationOptions
from battlegrounds.models import Battleground

class PageTranslationOptions(TranslationOptions):

    fields = ('title', 'description', 'title_min1', 'title_min2', 'title_min3', 'desc1', 'desc2', 'desc3' )

translator.register(Battleground, PageTranslationOptions)