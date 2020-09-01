from django.shortcuts import render
from battlegrounds.models import Battleground
from django.views.generic import ListView, DetailView


class Bgindex(ListView):
    model = Battleground
    template_name = 'battlegrounds/index.html'
    context_object_name = 'bg'


class Bg(DetailView):
    model = Battleground
    template_name = 'battlegrounds/base.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
