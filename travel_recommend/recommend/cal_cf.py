#협업 필터링 기반 추천

from .models import Tresult, Treview, Tuser, Travel
from .cal_knn import Cal_Knn 

user_id = 1

def start(result):
    user_no = user_id
    place1 = result[1]
    sql = 'insert into tresult(user_no, ) values()'
    date1 = Tresult.objects.filter('udate')    
    date2 = Treview.objects.filter('udate')
    results = Cal_Knn(user_id)


    return 'success'






