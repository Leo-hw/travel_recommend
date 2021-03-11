from .views import showme
from django.urls import path


urlpatterns = [
    path('showme/', showme),
    
]
