from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def view_cart(request):
    return render(request, "cart.html")


def add_cart(request, id):
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + 1
    else:
        cart[id] = cart.get(id, 1)

    request.session['cart'] = cart

    return redirect('shop:all_shop_works')


def remove_cart(request, id):
    cart = request.session.get('cart', {})

    cart[id] = int(cart[id]) - 1

    request.session['cart'] = cart

    return redirect('cart:view_cart')


def adjust_cart(request):
    return render(request, "cart.html")
