from heroes.models import Hero
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    hero = Hero.objects.all()
    context = {'hero': hero}
    return render(request, 'heroes/index.html', context)


class Heroes(DetailView):
    model = Hero
    template_name = 'heroes/base.html'
    slug_field = 'title_en'
    slug_url_kwarg = 'title_en'
