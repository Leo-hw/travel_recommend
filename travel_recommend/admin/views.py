from django.shortcuts import render

# Create your views here.


### make admin application for admin page
from django.views.generic import CreateView, ListView
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView

class AdminReviewCreate(CreateView):
    pass

class AdminReviewUpdate(UpdateView):
    pass

class AdminReviewDelete(DeleteView):
    pass

class ConnectProduct(View):
    pass

class ViewAvenue(ListView):
    
    pass


# 여기에 관리자용 페이지도 만들어서... 관리자가 리뷰 관리할 수 있도록 해야겠다.
# 그리고 추가적으로 여행 상품이랑 연계해서 팔 수 있도록.
# 관리자 페이지에서 수익이나 상품 관리도 하게 만들고
# 그러네 ... 그냥 원래 우리가 했던 페이지에다가 데이터 분석같은 것만 조금 가미한 상태로 만들면 되는 건데 너무 거창한 거 해보겠다고 한거였네....

