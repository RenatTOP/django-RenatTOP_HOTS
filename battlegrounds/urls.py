from . import views
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


app_name = 'battlegrounds'

urlpatterns = [
    path('', views.Bgindex.as_view(), name='index'),
    path('<url>/', views.Bg.as_view(), name='bg'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
