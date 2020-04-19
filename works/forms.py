from django import forms
from works.models import categories


class FilterForm(forms.Form):
    cat = forms.ModelChoiceField(
        queryset=categories.objects.all(), empty_label="-- Filter categories --")

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['cat'].label = False
