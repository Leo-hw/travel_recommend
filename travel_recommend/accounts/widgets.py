from django import forms
from django.forms import widgets
from recommend.models import Travel

class TownListSelect(forms.Select):
    model = Travel

    towns = list(Travel.objects.values_list('town', flat = True).distinct())
    town = forms.CharField(label = 'town', widget=forms.Select(choices=towns))
    #print(towns)
