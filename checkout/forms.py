from django import forms
from .models import orders
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, LayoutObject


class PaymentForm(forms.Form):
    """
    Form to handle the stripe payment
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4 er-form-padding'
        self.helper.field_class = 'col-sm-8 er-form-padding'
        self.helper.add_input(
            Submit('commit', 'Place order', css_id='submit_payment_btn', css_class='er-green'))
