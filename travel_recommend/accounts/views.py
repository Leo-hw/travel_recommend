import os,sys,inspect
currentdir = os.path.accounts(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.travel_recommend(currentdir)
sys.path.insert(0,parentdir) 

from .recommend.models import Travel




from .forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.models import User



# function for signup.
# manage accounts. login/logout and modify user info
def signup(request):
    tlist = Travel.objects.filter('town')
    clist = Travel.objects.filter('city')
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit = False)
            user_instance.set_password(signup_form.cleaned_data['password'] )
            user_instance.save()
            return render(request, 'accounts/singup_complete.html', {'username':user_instance.username})

    else:
        signup_form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form':signup_form.as_p, 'tlist':tlist, 'clist':clist})

# 여기에 관리자용 페이지도 만들어서... 관리자가 리뷰 관리할 수 있도록 해야겠다.
# 그리고 추가적으로 여행 상품이랑 연계해서 팔 수 있도록.
# 관리자 페이지에서 수익이나 상품 관리도 하게 만들고
# 그러네 ... 그냥 원래 우리가 했던 페이지에다가 데이터 분석같은 것만 조금 가미한 상태로 만들면 되는 건데 너무 거창한 거 해보겠다고 한거였네....

