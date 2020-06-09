from django import forms
from works.models import categories
from crispy_forms.helper import FormHelper


class FilterForm(forms.Form):
    cat = forms.ModelChoiceField(
        queryset=categories.objects.all(), empty_label="Filter categories")

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.fields['cat'].label = False
