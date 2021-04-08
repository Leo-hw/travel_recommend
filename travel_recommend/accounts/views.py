from django.views.generic.edit import DeleteView, UpdateView
from recommend.models import Travel

from .forms import SignUpForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

# function for signup.
# manage accounts. login/logout and modify user info
def signup(request):
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
        
        # else:
        #     return render(request, 'accounts/signup.html', {'form':signup_form.as_p})

    else:
        #request = request.GET
        signup_form = SignUpForm() 
        #print('else error')
                
    return render(request, 'accounts/signup.html', {'form':signup_form, 'town':town, 'city':city, 'site':site})
