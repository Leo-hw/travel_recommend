from .views import ReviewCreate, ReviewDelete, Top5Site, calculate
from django.urls import path

app_name = "recommend"
print('urls실행')
urlpatterns = [
    
    path('', Top5Site.as_view(), name = 'index'),
    path('reviewcreate/', ReviewCreate.as_view(), name = 'reviewcreate'),
    path('reviewdelete/', ReviewDelete.as_view(), name = 'reviewdelete'),


]
