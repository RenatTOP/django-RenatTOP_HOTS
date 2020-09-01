from django.shortcuts import render
from battlegrounds.models import Battleground
from heroes.models import Hero
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


def index(request):
    hero = Hero.objects.filter(title_en__in=['Imperius', 'Deathwing'])
    context = {'hero': hero}
    return render(request, 'home/index.html', context)

def agreement(request):
    return render(request, 'home/agreement.html')

class Username(DetailView):
    model = User
    template_name = 'home/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

def sitemap(request):
    hero = Hero.objects.filter
    bg = Battleground.objects.all()
    tank = hero(hero_type_en="tank")
    bruiser = hero(hero_type_en="bruiser")
    melee = hero(hero_type_en="melee assassin")
    ranged = hero(hero_type_en="ranged assassin")
    support = hero(hero_type_en="support")
    healer = hero(hero_type_en="healer")
    context = { 'bg'      :  bg,
                'tank'    :  tank,
                'bruiser' :  bruiser,
                'melee'   :  melee,
                'ranged'  :  ranged,
                'support' :  support,
                'healer'  :  healer}
    return render(request, 'home/sitemap.html', context)

def feedback(request):
    return render(request, 'home/feedback.html')

def favourite_hero(request, username, fav_id):
    hero = get_object_or_404(Hero, id=fav_id)
    if request.method == 'POST':
        hero.users.add(request.user)
    return render(request, 'home/profile.html')

def favourite_bg(request, username, fav_id):
    bg = get_object_or_404(Battleground, id=fav_id)
    if request.method == 'POST':
        bg.users.add(request.user)
    return render(request, 'home/profile.html')


def del_favourite_hero(request, username, fav_id):
    hero = get_object_or_404(Hero, id=fav_id)
    if request.method == 'POST':
        hero.users.remove(request.user)
    return render(request, 'home/profile.html')

def del_favourite_bg(request, username, fav_id):
    bg = get_object_or_404(Battleground, id=fav_id)
    if request.method == 'POST':
        bg.users.remove(request.user)
    return render(request, 'home/profile.html')