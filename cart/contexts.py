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
        work = get_object_or_404(work_items, pk=id)
        total += quantity * work.shop_settings.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'work': work})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
