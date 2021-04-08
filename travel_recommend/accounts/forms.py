from re import T
from django import forms
from django.forms import fields
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
    model = Travel
        
    # define fields 
    username = forms.CharField(label = 'username', widget=forms.TextInput, required=True)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput, required= True)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput, required= True)
    #site  = forms.CharField(label='name', widget=forms.TextInput, required= True)
    jumin = forms.IntegerField(label = 'jumin', required=True)
    gen = forms.IntegerField(label='gen', required=True, validators=[MinValueValidator(1), MaxValueValidator(9)])
    #occupations ={'선택하세요', '경영, 사무','생산, 제조','영업, 고객상담','전문직','IT, 인터넷','교육' ,'미디어','특수계층, 공공','건설','유통, 무역','서비스','디자인','의료','학생','주부','기타'}
    occupation = forms.CharField(label='occupation')
    #email = forms.EmailField(label='이메일', widget=forms.EmailInput)
    rating = forms.IntegerField(label='rating', required = True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    
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
        
    #도시
    sql = "select distinct(city) from travel"
    cursor.execute(sql)
    conn.commit() 
    
    cits = cursor.fetchall()
    cities = []
    for c in cits:
        cities.append(c)
    #cities = cursor.fetchall() 
    city = forms.CharField(label = 'city', widget=forms.Select(choices=cities))
    
    #동
    sql2 = "select distinct(town) from travel"
    cursor.execute(sql2)
    tows = cursor.fetchall()
    towns = []
    for t in tows:
        towns.append(t)
    #towns = cursor.fetchall()
    town = forms.CharField(label = 'town', widget=forms.Select(choices=towns))
    
    #여행지명
    sql3 = "select distinct(name) from travel"
    cursor.execute(sql3)
    #travel_sites = cursor.fetchall()
    travel_sites = []
    travel_s = cursor.fetchall()
    for ts in travel_s:
        travel_sites.append(ts)
    travel_name = forms.CharField(label = 'travel_name', widget=forms.Select(choices=travel_sites))
    
    cursor.close()
    conn.close()
    '''

    class Meta:
        model = User
        
        # fields = ['username', 'password','repeat_password', 'name','jumin','gen', 'occupation','email', 'rating', 'city', 'town', 'travel_name']
        # fields = ['username', 'password','repeat_password', 'name','jumin','gen', 'occupation','email', 'rating', 'city', 'town']
        fields = '__all__'

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']
 