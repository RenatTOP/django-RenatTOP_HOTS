from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'rating_matches'

urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
