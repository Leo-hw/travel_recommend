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
    
    #cursor = conn.cursor()
    town_list = []
    trave_sites = []
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        towns = self.request.session['town']
        traves = self.request.session['travel_site']
        
        print(towns)
        for t in towns:
            town_list.append(t['town'])
        for tr in traves:
            trave_sites.append(tr['travel_site'])
        self.fields['town'].choices = town_list
        self.fields['travel_site'].choices = trave_sites

        return town_list, trave_sites

    town = forms.ChoiceField(choices=town_list, required=True)
    travel_site = forms.ChoiceField(choices=trave_sites)
    # define fields 
    username = forms.CharField(label = 'username', widget=forms.TextInput, required=True)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput, required= True)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput, required= True)
    name  = forms.CharField(label='name', widget=forms.TextInput, required= True)
    jumin = forms.IntegerField(label = 'jumin', required=True)
    gen = forms.IntegerField(label='gen', required=True, validators=[MinValueValidator(1), MaxValueValidator(9)])
    occupation = forms.IntegerField(label='occupation')
    email = forms.EmailField(label='email', widget=forms.EmailInput)
    rating = forms.IntegerField(label='rating', required = True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    cities = list(Travel.objects.values_list('city', flat = True).distinct())
    city = forms.CharField(label = 'city', widget=forms.Select(choices=cities))
    #print(cities)
    
    # towns = list(Travel.objects.values_list('town', flat = True).distinct())
    # town = forms.CharField(label = 'town', widget=forms.Select(choices=towns))
    # print(towns)

    # travel_sites = list(Travel.objects.values_list('name', flat = True).distinct())
    # travel_site = forms.CharField(label = 'travel_site', widget=forms.Select(choices=travel_sites))
    # print(travel_sites)
    
    """
    class FooForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(FooForm, self).__init__(*args, **kwargs)
        bars = self.request.session['bars']
        foo_list = []
        for bar in bars:
            foo_list.append((bar['id'], bar['name']),)
        self.fields['foo'].choices = foo_list
    foo = forms.ChoiceField(choices=foo_list, required=True)
    """
    
    
    '''
    #도시
    sql = "select distinct(city) from travel"
    cursor.execute(sql)
    conn.commit() 
    
    cits = cursor.fetchall()
    cities = []
    for c in cits:
        cities.append(c)
    #cities = 
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
        
        # fill out fields with values for signup
        # can be added another field
        # fields = ['username', 'password','repeat_password', 'name','jumin','gen', 'occupation','email', 'rating', 'city', 'town', 'travel_name']
        
        # fields = ['username', 'password','repeat_password', 'name','jumin','gen', 'occupation','email', 'rating', 'city', 'town']
        fields = '__all__'

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']
 