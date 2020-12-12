from django import forms
from heroes.models import Hero
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.translation import gettext
from battlegrounds.models import Battleground
from django.core.mail.message import BadHeaderError
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    hero = Hero.objects.filter(title_en__in=['Malfurion', 'Valla', 'Gazlowe', 'Johanna',
                                            'Thrall', 'Dehaka', 'Tychus', 'Fenix', 'Whitemane',
                                            'Sylvanas', 'Malthael', 'Deckard', 'Ana', 'Orphea'])
    context = {'hero': hero}
    return render(request, 'home/index.html', context)


def agreement(request):
    return render(request, 'home/agreement.html')


class Profile(DetailView):
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
    context = {'bg':  bg,
               'tank':  tank,
               'bruiser':  bruiser,
               'melee':  melee,
               'ranged':  ranged,
               'support':  support,
               'healer':  healer}
    return render(request, 'home/sitemap.html', context)


class FeedbackForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message'] + "\n From: " + sender
            recipients = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                msg = gettext("Your message has not been sent")
                messages.error(request, msg)
                return redirect(request.path)
        msg = gettext("Your message has been sent")
        messages.success(request, msg)
        return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'home/feedback.html', {'form': form})


@login_required
def favourite_hero(request, fav_id):
    hero = get_object_or_404(Hero, id=fav_id)
    if request.method == 'POST':
        hero.users.add(request.user)
    return render(request, 'home/profile.html')


@login_required
def favourite_bg(request, fav_id):
    bg = get_object_or_404(Battleground, id=fav_id)
    if request.method == 'POST':
        bg.users.add(request.user)
    return render(request, 'home/profile.html')


@login_required
def del_favourite_hero(request, fav_id):
    hero = get_object_or_404(Hero, id=fav_id)
    if request.method == 'POST':
        hero.users.remove(request.user)
    return render(request, 'home/profile.html')


@login_required
def del_favourite_bg(request, fav_id):
    bg = get_object_or_404(Battleground, id=fav_id)
    if request.method == 'POST':
        bg.users.remove(request.user)
    return render(request, 'home/profile.html')
