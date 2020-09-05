from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler400, handler403, handler404, handler500



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
    path('accounts/change_password/', views.change_password, name='change_password'),
)

handler400 = 'renattop.views.page_400'
handler403 = 'renattop.views.page_403'
handler404 = 'renattop.views.page_404'
handler500 = 'renattop.views.page_500'