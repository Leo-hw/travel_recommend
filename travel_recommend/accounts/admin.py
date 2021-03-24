'''
import importlib
module = importlib.load_module('C:/work/recom/travel_recommend/travel_recommend/recommend/models.py')
module.function()
'''
from recommend.models import Travel, Treview
from django.contrib import admin
from .forms import SignUpForm

class ChoiceInline(admin.StackedInline):
    model = Travel
    extra = 3

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['review_text']}),
        ('Date information', {'fields': ['pub_date']}),
        (None, {'fields': ['review_title']}),
    ]

admin.site.register(Treview, ReviewAdmin)

@admin.register(Travel)
class StarAdmin(admin.ModelAdmin):
    form = SignUpForm

