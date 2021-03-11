from .views import signup
from django.urls import path


urlpatterns = [
    path('signup/', signup),
 
]
