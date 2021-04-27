from django.contrib.auth import views
from .views import ShowOcc, getTravelSite, signup, viewOcc
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/',  LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/',  LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    #path('showocc/',  ShowOcc.as_view(template_name = 'accounts/show_occ.html'), name = 'showocc'),
    path('showocc/',  viewOcc, name = 'showocc'),
    path('travel_site', getTravelSite),
]
