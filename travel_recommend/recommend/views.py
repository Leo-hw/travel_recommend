from .cal_knn import Cal_Knn
from django.contrib import messages
from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView
from .models import Travel, Treview, Tuser
from django.shortcuts import redirect, render
from django.views.generic.list import ListView


# Create your views here.
def showme(*args):
    rate = Tuser.objects.all()
    print(rate)

showme()

# function and class 
'''
1. first page ( best? popular 5)
2. search
3. 
'''

# 첫화면에 띄울 거, best.html
class Top5Site(ListView):
    model = Travel
    template_name_suffix = '_best'


#signup 은 accounts 쪽으로 넣고
# 여기는 계산하는 거랑 날씨 불러오기
#로그아웃 로그인은 장고 기본으로 사용
# 디테일 눌렀을 때, 흠... 가져와서 보여주기

# 회원 가입시 리뷰 기본적으로 설정하도록 하고 - 선택적으로 할 수 있게
# 만약에 리뷰를 안하면, best 여행지만 show하고

# 리뷰 추가 기능

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

        # 여기 author 를 잘못된 거 같은데....?
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

  
# 흠...
# 계산용 search 로 만들고
# knn/ svm
# 또 뭐가 있남...CNN도 값을 더주고 하면 될 거 같기는 한데...

# 얘는 그냥 펑션으로만 해야겠는데...? 이게 되나?

# 검색 할 때는, 유저들 위주로 보여주고, if 문으로 로그인이 된(회원이면, 본인 리뷰 쓴 거 기반으로 보여주면 되니가)
# 아닌 경우에는 검색할 때, 가장 많은 유저들이 방문한 장소를 보여주면 되지 않을까?
# 도시를 일단 입력하면 도시는 있으니,까, 도시 내에서 가장 방문수가 많은 곳으로 가면 되겠지.
# 아 근데 이러면 오래 걸리잖아....???????? visit_count 컬럼도 하나 만들어서 방문수도 넣어야하나....?
# city town 나오는데...?
# 이렇게 하면, 자료가 적어서 town (도시)로 했는데, 자료갯수가 적다.
# 그래서 안될 거 같은데...?
# city가 도시가 아니라 도, 행정구역 구분인데, 흠... 
# 아니면 아예 로그인 안한 상태에서는 검색 창이 안보이고
# 그냥 그런 거지, 도 별로 버튼 누를 수 있게 해두고, 베스트 여행지만 누를 수 있도록 하는거, 이거는 회원한테도 보이게 해도 상관없겠다.
# 그냥 그거를 메인 페이지에 넣으면 되겠다.
# 사실은 여기다가 모든 거 다 예약할 수 있게 더 하면 좋은데
# 이건 뭐 그냥 내 욕심
# admin 페이지에서 travel 업데이트 하도록 해야하

def calculate(request):
    # 여기서 request.user_id 받아서 tuser.user_id 랑 같은 지 비교해보고 is_valid()로 
    # kal knn/ svm / 
    
    results = Cal_Knn(request)
    print(results[0]['iid'].values)    
    tlist = results[0]['iid'].values
        
    flist = []
    for f in tlist :
        tour = Travel.objects.filter(placeId = f)
        flist.append(" ".join(tour))
    print(flist)
        

    return render(request, 'calculate.html', {'tour':flist})

class CalculateReview(View):
    # Rmodel = Treview
    # Umodel = Tuser
    # Tmodel = Travel

    
    model = Treview
    template_name_suffix = 'calculate.html'
    
    # 얘를 여기다가 넣을게 있을까...?
    # 그냥 계산하는 거니까 굳이....????
    #def cal_knn(self, request):
        #다른 거 굳이 넣을 필요있남?
        #request.tourid = self.



