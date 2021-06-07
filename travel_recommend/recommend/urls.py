from .views import ReviewCreate, ReviewDelete, Top5Site, search, recom
from django.urls import path

app_name = "recommend"
#print('urls실행')
urlpatterns = [
    
    # 리뷰 리스트 보기 - top5 여행지 인기도 순
    path('', Top5Site.as_view(), name = 'index'),
    #
    path('reviewcreate/', ReviewCreate.as_view(), name = 'create'),
    path('reviewdelete/', ReviewDelete.as_view(), name = 'delete'),
    path('reviewdetail/', ReviewCreate.as_view(), name = 'create'),
    # 리뷰 like
    path('reviewlike/', ReviewCreate.as_view(), name = 'create'),
    # 여행지 검색
    path('recom/', search, name = 'recom'),
    
]
