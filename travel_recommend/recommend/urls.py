from .views import ReviewCreate, ReviewDelete, Top5Site, search
from django.urls import path

app_name = "recommend"
print('urls실행')
urlpatterns = [
    # with out login
    path('', Top5Site.as_view(), name = 'index'),

    path('reviewcreate/', ReviewCreate.as_view(), name = 'create'),
    path('reviewdelete/', ReviewDelete.as_view(), name = 'delete'),
    path('search/', search, name = 'search'),
    #like list -  #path('reviewdelete/', .as_view(), name = ''),
    # list  #path('reviewdelete/', .as_view(), name = ''),
]
