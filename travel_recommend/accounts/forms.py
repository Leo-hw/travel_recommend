from recommend.models import Travel
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class SignUpForm(forms.ModelForm):
    model = Travel
    password = forms.CharField(label = 'password', widget=forms.PasswordInput, required= True)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput, required= True)
    rating = forms.IntegerField(label='rating', required = True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    #travel_id = forms.CharField(label = 'travel_id', widget=forms.TextInput)
    city = forms.CharField(label = 'city', widget=forms.Select(
        attrs={
            "placeholder": "select",
            "values":{1,2,3,4,5},
            }))
    town = forms.CharField(label = 'town', widget=forms.Select)
    travel_name = forms.CharField(label = 'travel_name', widget=forms.Select(
        attrs={
            "placeholder": "select",
            "values":{1,2,3,4,5},
            
        }

    ))


    class Meta:
        model = User
        
        # fill out fields with values for signup
        # can be added another field
        #fields = ['username', 'password','password2', 'first_name', 'last_name', 'email', 'rating', 'city', 'town']
        fields = '__all__'
        # widgets = {
        #     'rating': starWidget,
        # }

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']
