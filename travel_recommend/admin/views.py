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


# 그러네 ... 그냥 원래 우리가 했던 페이지에다가 데이터 분석같은 것만 조금 가미한 상태로 만들면 되는 건데 너무 거창한 거 해보겠다고 한거였네....

