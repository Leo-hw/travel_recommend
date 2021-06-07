from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Occupations
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from recommend.models import Travel
from django.contrib import messages
from .forms import OccuForm, SignUpForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

# function for signup.
# manage accounts. login/logout and modify user info

class UserLoginView(LoginView):           # 로그인
    template_name = 'user/login.html'
    
    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)    


def signup(request):

    # login 된 상태에서 접근 안되도록 막아야 함.

    town = list(Travel.objects.values_list('town', flat = True).distinct())
    city = list(Travel.objects.values_list('city', flat = True).distinct())
    site = list(Travel.objects.values_list('site', flat = True).distinct())
    
    # should be modified with ajax or using widgets of django
    # => to react 
    #print(site)
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, Travel)
        print('views.error')
        if signup_form.is_valid():
            print("instance error")
            user_instance = signup_form.save(commit = False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request, 'accounts/singup_complete.html', {'username':user_instance.username})
        
        
    else:
        #request = request.GET
        signup_form = SignUpForm() 
        #print('else error')
    return render(request, 'accounts/signup.html', {'form':signup_form, 'town':town, 'city':city, 'site':site})

class ShowOcc(ListView):
    model = Occupations 
    form_class = OccuForm
    #template_name = 'show_occ.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         messages.warning(request, 'Please login, this service needs login before')
    #         return HttpResponseRedirect('/')
    #     return super(ShowOcc, self).dispatch(request, *args, **kwargs)

def viewOcc(request):
    #print('viewOcc 실행')
    model = Occupations
    form_class = OccuForm
    #print('여기는 뷰스',form_class)
    return render(request,'accounts/show_occ.html',{'form':form_class} )

def getTravelSite(request):
    area = request.GET['area']
    way = request.GET['way']
    #print(area, way)
    city = area.split()[0]
    if len(area.split()) == 3:
        town = area.split()[1] + " " + area.split()[2]
    else:
        town = area.split()[1]
    #print(town)
    if way == 'food':
        travel_near = Travel.objects.filter(city = city,town = town, genre__lte = 2).order_by('-tscore')
    elif way == 'place':
        travel_near = Travel.objects.filter(city = city,town = town, genre__gt = 2).order_by('-tscore')
    datas = []
    for tn in travel_near:
        dic = {'tour':tn.tourname, 'area':area, 'genre':tn.genre.genrename, 'cnt':tn.count, 'score':tn.score}
        datas.append(dic)
    return HttpResponse(json.dumps(datas), content_type = "application/json")
