from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from accounts.decorators import admin_only
from works.models import work_items, work_images
from shop.models import shop_items, shipping, shop_message
from checkout.models import orders, order_items
from dashboard.forms import SetShopMessageForm

# Create your views here.


@login_required()
@admin_only
def list_orders(request, filter=None):
    """
    Display a list of all orders
    With links to their details pages
    """

    # Get all orders
    all_orders = orders.objects.all().order_by('paid', 'sent', '-date')
    title = 'Viewing all orders'
    return render(request, "listorders.html",
                  {'title': title,
                   'orders': all_orders})


@login_required()
@admin_only
def view_order(request, pk):
    """
    Display the details of an order
    With buttons to update shipping/ payment status
    """

    next = request.GET.get('next', '/')
    # Check if this order exists
    try:
        order = orders.objects.get(pk=pk)
    # if not show the list and rais an error message
    except:
        messages.error(request,
                       'This order does not exist')
        return redirect(next)
    # Check if there are order items
    try:
        items = order_items.objects.filter(order=order)
    # If not show the list and raise an error message
    except:
        messages.error(request,
                       'This order does not have any items')
        return redirect(next)
    title = 'Viewing order'
    return render(request, "vieworder.html", {'title': title,
                                              'order': order,
                                              'items': items,
                                              'next': next})


@login_required()
@admin_only
def update_order(request, pk, action=None):
    """
    Change the shipping/payment status of an order
    """

    next = request.GET.get('next', '/')
    # Check if this is an existing order
    try:
        order = orders.objects.get(pk=pk)
    # If not Show the list and raise an error message
    except:
        messages.error(request,
                       'This order does not exist')
        return redirect('dashboard:list_orders')
    # Check wich attributes needs to be updated and save the object
    if action == 'paid':
        order.paid = True
        order.save()
        messages.success(request,
                         'The order was marked as paid')
        return redirect(next)
    elif action == 'notpaid':
        order.paid = False
        order.save()
        messages.success(request,
                         'The order was marked as not paid')
        return redirect(next)
    elif action == 'sent':
        order.sent = True
        order.save()
        messages.success(request,
                         'The order was marked as sent')
        return redirect(next)
    elif action == 'notsent':
        order.sent = False
        order.save()
        messages.success(request,
                         'The order was marked as not sent')
        return redirect(next)
    elif action == 'delete':
        order.delete()
        messages.success(request,
                         'The order was successfully deleted')
        return redirect(next)
    else:
        return redirect('dashboard:list_orders')


@login_required()
@admin_only
def set_shop_order(request, pk):
    """
    Set the display order for shop view
    """

    # Check if this work exists
    try:
        work = work_items.objects.get(pk=pk)
    except:
        # if not return to the works list
        messages.error(request, 'This work does not exist')
        return redirect('dashboard:list_works')
    # Get the new sort_order and update object
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        order = request.POST.get("sort_order")
        work.shop_settings.sort_order = order
        work.shop_settings.save()
        messages.success(request,
                         'Display order in the shop of ' +
                         work.title + ' has been updated')
    return redirect(next)


@login_required()
@admin_only
def set_image_order(request, pk):
    """
    Set the display order for extra images
    """

    # Check if this work exists
    try:
        image = work_images.objects.get(pk=pk)
    except:
        # if not return to the works list
        messages.error(request,
                       'This image does not exist')
        return redirect('dashboard:list_works')
    # Get the new sort_order and update object
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        order = request.POST.get("sort_order")
        image.sort_order = order
        image.save()
        messages.success(
            request,
            'Display order of this image has been updated')
    return redirect(next)


@login_required()
@admin_only
def set_shop_image(request, pk):
    """
    Set an image as default for the shop
    """

    next = request.GET.get('next', '/')
    try:
        image = work_images.objects.get(pk=pk)
    except:
        messages.error(request,
                       'This image does not exist')
        return redirect(next)
    try:
        shop = image.work_item.shop_settings
        shop.main_image = image
        shop.save()
        messages.success(request,
                         'Image set as shop default')
    except:
        messages.error(request,
                       'This is not a shop item')
        return redirect(next)
    return redirect(next)


@login_required()
@admin_only
def unset_shop_image(request, pk):
    """
    unset default image for the shop
    """

    next = request.GET.get('next', '/')
    # Check if this shop item exists
    try:
        shop_item = shop_items.objects.get(pk=pk)
    except:
        messages.error(request,
                       'This image does not exist')
        return redirect(next)
    # Unset custom main image (work main image will be used)
    shop_item.main_image = None
    shop_item.save()
    messages.success(request,
                     'Shop main image was reset to work main image')
    return redirect(next)



@login_required()
@admin_only
def edit_settings(request):
    """
    Edit shop settings
    """
    # Get shop message object and create form
    try:
        message = shop_message.objects.first()
        message_form = SetShopMessageForm(instance=message)
    except:
        # Create empty form
        message_form = SetShopMessageForm()

    # Get all shipping regions
    shippings = shipping.objects.all()

    title = 'Adjust shop settings'
    return render(request, "settings.html",
                  {'title': title,
                   'message_form': message_form,
                   'shippings': shippings})


@login_required()
@admin_only
def set_shop_message(request):
    """
    Set shop message
    """
    # check if there already is an object
    try:
        message = shop_message.objects.first()
    except:
        message = None
    if request.method == 'POST':
        # Get the form
        message_form = SetShopMessageForm(
            request.POST, instance=message)
        next = request.POST.get('next', '/')
        if message_form.is_valid():
            # Save the message to the database
            message_form.save()
            return redirect(next)
        else:
            return redirect(next)
    else:
        return redirect('dashboard:edit_settings')

