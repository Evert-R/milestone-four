from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from works.models import work_items, work_images
from shop.models import shop_items, work_types, work_sizes, materials
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, LayoutObject


class EditWorksForm(ModelForm):
    class Meta:
        model = work_items
        fields = ['main_image', 'position', 'category', 'title',
                  'under_title', 'free_text', 'work_item', 'shop_item', 'sort_order']
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
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4 er-form-padding'
        self.helper.field_class = 'col-sm-8 er-form-padding'
        self.helper.add_input(
            Submit('submit', 'Submit work details', css_class='er-green'))


class EditShopWorksForm(ModelForm):
    class Meta:
        model = shop_items
        fields = ['price', 'stock', 'edition_count', 'work_type', 'material', 'work_size', 'frame',
                  'signed', 'personal_message', 'standard_text', 'personal_text', 'sort_order']
        widgets = {
            'personal_message': Textarea(attrs={'cols': 10, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(EditShopWorksForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4 er-form-padding'
        self.helper.field_class = 'col-sm-8 er-form-padding'
        self.helper.add_input(
            Submit('submit', 'Submit shop details', css_class='er-green'))


class AddExtraImagesForm(ModelForm):
    class Meta:
        model = work_images
        fields = ['work_item', 'work_image']
        widgets = {
            'work_item': forms.HiddenInput()
        }
        labels = {
            'work_image': _('Add image'),
        }

    def __init__(self, *args, **kwargs):
        super(AddExtraImagesForm, self).__init__(*args, **kwargs)
        self.fields['work_item'].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4 er-form-padding'
        self.helper.field_class = 'col-sm-8 er-form-padding'
        self.helper.add_input(
            Submit('submit', 'Submit extra image', css_class='er-green'))
