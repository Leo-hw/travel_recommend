from .forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit = False)
            user_instance.set_password(signup_form.cleaned_data['password'] )
            user_instance.save()
            return render(request, 'accounts/singup_complete.html', {'username':user_instance.username})

        else:
            signup_form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form':signup_form.as_p})
