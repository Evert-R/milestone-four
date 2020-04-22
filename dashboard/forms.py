from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from works.models import work_items
from shop.models import shop_items, work_types, work_sizes, materials
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, LayoutObject


class EditWorksForm(ModelForm):
    class Meta:
        model = work_items
        fields = ['main_image', 'position', 'category', 'title',
                  'under_title', 'free_text', 'work_item', 'shop_item']
        widgets = {
            'free_text': Textarea(attrs={'cols': 10, 'rows': 10}),
        }
        labels = {
            'free_text': _('Description'),
        }
        help_texts = {
            'position': _('Choose work view lay-out'),
        }

    def __init__(self, *args, **kwargs):
        super(EditWorksForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.add_input(Submit('submit', 'Submit'))


class EditShopWorksForm(ModelForm):
    class Meta:
        model = shop_items
        fields = ['work_item', 'price', 'stock', 'edition_count', 'frame',
                  'signed', 'work_type', 'material', 'work_size']

    def __init__(self, *args, **kwargs):
        super(EditShopWorksForm, self).__init__(*args, **kwargs)
        self.fields['work_item'].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.add_input(Submit('submit', 'Submit'))
