from django.views.generic.edit import DeleteView, UpdateView
# file_2.py
import sys
sys.path.append('/.../travel_recommend/recommend/')
#import models 

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

