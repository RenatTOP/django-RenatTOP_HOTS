from heroes.models import Hero
from modeltranslation.translator import translator, TranslationOptions


class PageTranslationOptions(TranslationOptions):

    fields = ('title', 'title_min', 'description', 'hero_type', 'ability1', 'ab_desc1',
              'ability2', 'ab_desc2', 'ability3', 'ab_desc3', 'heroic1', 'heroic_desc1',
              'heroic2', 'heroic_desc2', 'ab_trait', 'trait_desc')


translator.register(Hero, PageTranslationOptions)
