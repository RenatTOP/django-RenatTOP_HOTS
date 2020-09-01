from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'heroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<title_en>/', views.Heroes.as_view(), name='Heroes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
