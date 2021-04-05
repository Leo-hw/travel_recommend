from .weather import Weather
from .cal_knn import Cal_Knn
from django.contrib import messages
from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView
from .models import Travel, Treview, Tuser
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

print('views 실행')

# first page(index)
class Top5Site(ListView):
    model = Travel
    template_name_suffix = '_best'

# make detail function 

# 회원 가입시 리뷰 - 기본적으로 3~5 곳 설정 - 선택적으로 
# 리뷰를 안하면, best 여행지만 show하고

from django.views.generic import CreateView
class ReviewCreate(CreateView):
    model = Treview
    template_name_suffix = 'review_create.html'

    def from_valid(self, form):
        form.instance.author_id = self.request.user.id
        print(form.instance.author_id)
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class ReviewUpdate(UpdateView):
    model = Treview
    fields = ['rating', 'tourid']
    template_name_suffix = 'review_update.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()

        # 여기 author 확인 필요
        # 일단 여기부분은 django documentation 확인이 필요.
        
        if object.author != request.treview_id:
            messages.warning(request, "권한이 없습니다.")
            return HttpResponseRedirect('/')
        else:
            return super(ReviewUpdate, self).dispatch(request, *args, **kwargs)

class ReviewDelete(DeleteView):
    model = Treview
    template_name_suffix = 'review_delete.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()

        if object.author != request.treview_id:
            messages.warning(request, "권한이 없습니다.")
            return HttpResponseRedirect('/')
        else:
            return super(ReviewDelete, self).dispatch(request, *args, **kwargs)


# 처음 가입시에는 레이팅(별점)을 줄 수 있도록 하고, 본인이 다녀온 여행지에 대해서는 리뷰를 쓰게 하기 => 리뷰쓴 거를 보고 다른 사람이 다녀오면 혜택
# 리뷰에 연동되어있는 상품을 선택한 여행자에게는 할인 혜택
# 이런식으로 서로에게 혜택을 줄 수 있도록 만들면 되게ㅐㅆ다~ 좋다좋아...

# 검색 할 때는, 유저들 위주로 보여주고, if 문으로 로그인이 된(회원이면, 본인 리뷰 쓴 거 기반으로 보여주면 되니가)
# 아닌 경우에는 검색할 때, 가장 많은 유저들이 방문한 장소를 보여주면 되지 않을까?
# 도시를 일단 입력하면 도시는 있으니,까, 도시 내에서 가장 방문수가 많은 곳으로 가면 되겠지.
# 아 근데 이러면 오래 걸리잖아....???????? visit_count 컬럼도 하나 만들어서 방문수도 넣어야하나....?
# city town 나오는데...?

# 이렇게 하면, 자료가 적어서 town (도시)로 했는데, 자료갯수가 적다.
# 그래서 안될 거 같은데...?
# city가 도시가 아니라 도, 행정구역 구분인데, 흠... 
# 아니면 아예 로그인 안한 상태에서는 검색 창이 안보이고

# 도 별로 버튼 누를 수 있게 해두고, 베스트 여행지만 누를 수 있도록 하는거, 이거는 회원한테도 보이게 해도 상관없겠다.

# weather
def weather(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

    if start_date == '':
        start_date = None
        weather = ''
    if end_date == '':
        end_date = None
        weather = ''
        
    wlist = []
    # 날씨 출력  // 이거 수정해야한다던데..
    try:
        weather = Weather(search)
        query = (weather['date'] >= start_date) & (weather['date'] <= end_date)
        for i in range(len(weather.loc[query]['weather'].values)):
            w = weather.loc[query]['weather'].values[i]
            if (w >= 1 and w <= 3) or (w >= 33 and w <= 35):
                w = '맑음'
            elif (w >= 4 and w <= 5) or (w >= 36 and w <= 37):
                w = '구름 조금'
            elif (w >= 6 and w <= 8) or (w == 38):
                w = '흐림'
            elif (w == 11):
                w = '안개'
            elif (w == 12 or w == 13):
                w = '소나기'
            elif (w >= 14 and w <= 17) or (w == 39):
                if (w == 15 or w == 16) or (w == 41 or w == 42):
                    w = '천둥번개와 비'
                w = '한때 비'
            elif w == 18 and w <= 40:
                if (w >= 19 and w <= 21) or (w == 32):
                    w = '강풍'
                elif(w == 23 or w == 24) or (w == 29) or (w == 43 or w == 44):
                    w = '눈'
                elif(w == 25):
                    w = '진눈깨비'
                elif(w == 26):
                    w = '얼어붙은 비'
                w = '비'
            elif w == 30:
                w = '뜨거움 - 주의'
            elif w == 31:
                w = '추움 - 주의'
            wlist.append(w)
        print(wlist)   
    except: 
        print('===날짜가 없을경우===')

# 계산
def search(request):
    user_id = request.user.id
    #print(user_id)
    results = Cal_Knn(user_id)
    print(results[0]['iid'].values)    
    tlist = results[0]['iid'].values
        
    flist = []
    for f in tlist :
        tour = Travel.objects.filter(placeId = f)
        flist.append(" ".join(tour))
    print(type(flist))
    context = {'tour':flist}
    return render(request, 'search.html', context)

'''
treview
treview_no, treview_id, tourid, rating, genre 

tuser
tuser_no, tuser_id, tuser_occ, 
tuser_jumin, tuser_gender

travel
tourid, city, town, name, type1, type2, type3, genre

'''
