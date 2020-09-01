from django.shortcuts import render


def index(request):
    return render(request, 'brawl/base.html')

