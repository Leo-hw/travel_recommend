from re import T

from django.forms.models import ModelForm
from .models import Occupations
from .models import Tuser
from .widgets import TownListSelect, AutoCompleteWidget
from django import forms
from django.forms import fields, widgets
from recommend.models import Travel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
#from .models import User
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
conn = MySQLdb.connect(**config)

class SignUpForm(forms.ModelForm):
    model = Tuser
        
    # define fields 
    username = forms.CharField(label = 'username', widget=forms.TextInput, required=True)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput, required= True)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput, required= True)
    #site = forms.CharField(label='site', widget=forms.TextInput, required= True)
    jumin = forms.IntegerField(label = 'jumin', required=True)
    gen = forms.IntegerField(label='gen', required=True, validators=[MinValueValidator(1), MaxValueValidator(9)])
    #occupations = {'선택하세요', '경영, 사무','생산, 제조','영업, 고객상담','전문직','IT, 인터넷','교육' ,'미디어','특수계층, 공공','건설','유통, 무역','서비스','디자인','의료','학생','주부','기타'}
    
    #occupation = forms.CharField(label='occupation', required=True, widget=forms.Select(choices = occupations))
    occupation = forms.CharField(label='occupation', widget=AutoCompleteWidget)
    email = forms.EmailField(label='이메일', widget=forms.EmailInput)
    rating = forms.IntegerField(label='평점', required = True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # cities = list(Travel.objects.values_list('city', flat = True).distinct())
    # city = forms.CharField(label = 'city', widget=forms.Select(choices=cities))
    # print(type(city), city)
    # test = forms.ChoiceField(label = 'test', choices={'가', '나', '다'})
    '''
    towns = list(Travel.objects.values_list('town', flat = True).distinct())
    town = forms.CharField(label = 'town', widget=forms.Select(choices=towns))
    print(towns)

    travel_sites = list(Travel.objects.values_list('name', flat = True).distinct())
    travel_site = forms.CharField(label = 'travel_site', widget=forms.Select(choices=travel_sites))
    print(travel_sites)
    '''     
   
    class Meta:
        model = Tuser
        # fields = ['username', 'password','repeat_password', 'name','jumin','gen', 'occupation','email', 'rating', 'city', 'town', 'travel_name']
        fields = '__all__'
        widgets = {
        #    'town':TownListSelect,
            'occupation':AutoCompleteWidget,    
        }

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']
 

class OccuForm(ModelForm):
    class Meta:
        model = Occupations
        fields = ['occ']