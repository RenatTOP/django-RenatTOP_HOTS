from . import views
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.shortcuts import render, redirect


app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('agreement/', views.agreement, name='agreement'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('feedback/', views.feedback, name='feedback'),
    path('user/<username>', views.Username.as_view(), name='profile'),
    path('user/<int:fav_id>/add_fav_hero/', views.favourite_hero, name='favourite_hero'),
    path('user/<int:fav_id>/del_fav_hero/', views.del_favourite_hero, name='del_favourite_hero'),
    path('user/<int:fav_id>/add_fav_bg/', views.favourite_bg, name='favourite_bg'),
    path('user/<int:fav_id>/del_fav_bg/', views.del_favourite_bg, name='del_favourite_bg'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
