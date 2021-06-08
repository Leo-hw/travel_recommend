#협업 필터링 기반 추천

from .models import Tresult, Treview, Tuser, Travel
from .cal_knn import Cal_Knn 

user_id = 1

def Cal_Cf(user_id):
    user_no = user_id
    results = Cal_Knn(user_id)
    place1 = results[1]
    sql = 'insert into tresult(user_no,place1, place2, place3, place4, place5, udate) values(%s, %s, %s, %s, %s, %s, %s)'
    
    tresult = Tresult(udate='sysdate()')
    
    #date1 = Tresult.objects.filter('udate')    
    date2 = Treview.objects.filter('udate')


    return 'success'

start(user_id)






