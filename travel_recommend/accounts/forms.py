from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fill out fields with values for signup
        # can be added another field
        fields = ['username', 'password','password2', 'first_name', 'last_name', 'email']

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']
