from . import models
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

#user
# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):

#     list_display = (
#         'nickname',
#         'email',
#         'date_joined',
#     )

#     list_display_links = (
#         'nickname',
#         'email',
#     )