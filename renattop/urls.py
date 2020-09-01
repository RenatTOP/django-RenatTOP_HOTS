from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.utils.translation import gettext_lazy as _



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('brawl/', include('brawl.urls')),
    path('battlegrounds/', include('battlegrounds.urls')),
    path('game_modes/', include('game_modes.urls')),
    path('heroes/', include('heroes.urls')),
    path('rating_matches/', include('rating.urls')),
    path('roles/', include('roles.urls')),
    path('renattop-myadmin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.signup),
)