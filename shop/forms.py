from django import forms
from shop.models import work_types, work_sizes, materials
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, LayoutObject


class ShopFilterForm(forms.Form):
    type = forms.ModelChoiceField(
        queryset=work_types.objects.all(), empty_label="-- Type --", required=False)
    size = forms.ModelChoiceField(
        queryset=work_sizes.objects.all(), empty_label="-- Size --", required=False)
    mat = forms.ModelChoiceField(
        queryset=materials.objects.all(), empty_label="-- Material --", required=False)

    def __init__(self, *args, **kwargs):
        super(ShopFilterForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = False
        self.fields['size'].label = False
        self.fields['mat'].label = False
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'er-shop-field'
