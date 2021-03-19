from ...travel_recommend.recommend.models import Travel, Treview
from django.contrib import admin

# Register your models here.
from .models import Question


class ChoiceInline(admin.StackedInline):
    model = Travel
    extra = 3

class ReviewAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'review_title', 'review_text']

    fieldsets = [
        (None,               {'fields': ['review_text']}),
        ('Date information', {'fields': ['pub_date']}),
        (None, {'fields': ['review_title']}),
    ]

admin.site.register(Treview, ReviewAdmin)
