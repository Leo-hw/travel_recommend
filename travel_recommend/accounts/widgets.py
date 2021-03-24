from django import forms

# widget
# star widget
# select widget 추가.

class starWidget(forms.TextInput):
    input_type = 'rating'
    template_name = "widgets/star_rate.html"

    class Media:
        css = {
            'all': [
                'widgets/star_rate.html'
            ]
        }