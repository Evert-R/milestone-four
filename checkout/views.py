from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import PaymentForm
from .models import orders, order_items
from works.models import work_items
from accounts.models import user_details
from accounts.forms import UserDetailsForm
from django.conf import settings
from django.utils import timezone

import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def check_out(request):
    # Get logged in user
    active_user = request.user
    try:
        current_user_details = user_details.objects.get(user=active_user)
    except:
        # If not show shipping details form
        return redirect('accounts:shipping_details')
    # Attach user details to form
    accounts_form = UserDetailsForm(instance=current_user_details)
    # Check if a form was submitted
    if request.method == "POST":
        # Get both forms
        accounts_form = UserDetailsForm(
            request.POST, instance=current_user_details)
        payment_form = PaymentForm(request.POST)
        # If shipping details were changed update and return
        if accounts_form.is_valid():
            current_user_details = accounts_form.save()
            messages.success(request, 'Updated shipping details')
            return redirect('checkout:check_out')
        # if payment form is valid create order
        if payment_form.is_valid():
            order = orders(user=active_user,
                           date=timezone.now(),
                           )
            order.save()
            # Get cart contents
            cart = request.session.get('cart', {})
            total = 0
            # Create order items for order
            for id, quantity in cart.items():
                work_item = get_object_or_404(work_items, pk=id)
                total += quantity * work_item.shop_settings.price
                order_item = order_items(
                    order=order,
                    work_item=work_item,
                    quantity=quantity,
                    price=work_item.shop_settings.price
                )
                order_item.save()
            # Make payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                order.paid = True
                order.save()
                request.session['cart'] = {}
                return redirect(reverse('shop:all_shop_works'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = PaymentForm()
    return render(request, "checkout.html", {'accounts_form': accounts_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
