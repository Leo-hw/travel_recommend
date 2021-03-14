from .views import Top5Site, calculate, showme
from django.urls import path


urlpatterns = [
    path('showme/', showme),
    path('', Top5Site.as_view(), name = 'index'),
]
