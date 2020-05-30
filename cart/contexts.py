from django.shortcuts import get_object_or_404
from works.models import work_items


def cart_contents(request):
    """
    Create a cart available in all pages
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        # get work object
        work = get_object_or_404(work_items, pk=id)
        # Check if there is a discount
        if work.shop_settings.on_sale == True:
            price = work.shop_settings.discount_price
        else:
            price = work.shop_settings.price
        total += quantity * price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'work': work})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
