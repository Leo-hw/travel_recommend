from django.views.generic.edit import DeleteView, UpdateView
from recommend.models import Travel

from .forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.models import User

# function for signup.
# manage accounts. login/logout and modify user info
def signup(request):
    # 여기서 select 박스에 넣을 내용 미리 읽어서 보내기.    
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        # tlist = Travel.objects.filter('town')
        # clist = Travel.objects.filter('city')
        
        if signup_form.is_valid():
            user_instance = signup_form.save(commit = False)
            
            user_instance.set_password(signup_form.cleaned_data['password'])
            
            user_instance.save()
            return render(request, 'accounts/singup_complete.html', {'username':user_instance.username})

    else:
        signup_form = SignUpForm()
        # tlist = Travel.objects.filter('town')
        # clist = Travel.objects.filter('city')

    return render(request, 'accounts/signup.html', {'form':signup_form.as_p})
