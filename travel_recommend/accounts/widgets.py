from django import forms
from django.forms import widgets
from recommend.models import Travel

class TownListSelect(forms.Select):
    model = Travel
    towns = list(Travel.objects.values_list('town', flat = True).distinct())
    town = forms.CharField(label = 'town', widget=forms.Select(choices=towns))
    #print(towns)

class AutoCompleteWidget(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Media:
        css = {
            'all' : [
                "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/css/select2.min.css",
            ],
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/js/select2.min.js",
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs)
        context['style'] = 'min-width:200px;'
        return context