from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from works.models import work_items, categories, work_images
from shop.models import shop_items, work_sizes, work_types, materials
from checkout.models import orders, order_items
from dashboard.forms import EditWorksForm, EditShopWorksForm, AddExtraImagesForm
from accounts.decorators import admin_only

# Create your views here.


@login_required(login_url='accounts:log_in')
@admin_only
def list_orders(request, filter=None):
    """
    Display a list of all works
    With links to their edit pages
    Change display order of works
    """
    all_orders = orders.objects.all()
    title = 'Viewing all orders'
    return render(request, "listorders.html", {'title': title,
                                               'orders': all_orders})


@login_required(login_url='accounts:log_in')
@admin_only
def view_order(request, pk):
    """
    Display a list of all works
    With links to their edit pages
    Change display order of works
    """
    try:
        order = orders.objects.get(pk=pk)
    except:
        messages.error(request, 'This order does not exist')
        return redirect('dashboard:list_orders')
    try:
        items = order_items.objects.filter(order=order)
    except:
        messages.error(request, 'This order does not have any items')
        return redirect('dashboard:list_orders')
    title = 'Viewing order'
    return render(request, "vieworder.html", {'title': title,
                                              'order': order,
                                              'items': items})


@login_required(login_url='accounts:log_in')
@admin_only
def update_order(request, pk, action=None):
    """
    Display a list of all works
    With links to their edit pages
    Change display order of works
    """
    next = request.GET.get('next', '/')
    try:
        order = orders.objects.get(pk=pk)
    except:
        messages.error(request, 'This order does not exist')
        return redirect('dashboard:list_orders')
    if action == 'paid':
        order.paid = True
        order.save()
        return redirect(next)
    elif action == 'notpaid':
        order.paid = False
        order.save()
        return redirect(next)
    elif action == 'sent':
        order.sent = True
        order.save()
        return redirect(next)
    elif action == 'notsent':
        order.sent = False
        order.save()
        return redirect(next)
    elif action == 'notsent':
        order.sent = False
        order.save()
        return redirect(next)
    elif action == 'delete':
        order.delete()
        messages.success(request, 'The order was successfully deleted')
        return redirect(next)
    else:
        return redirect('dashboard:list_orders')


@login_required(login_url='accounts:log_in')
@admin_only
def list_works(request, filter=None):
    """
    Display a list of all works
    With links to their edit pages
    Change display order of works
    """

    if filter == 'work':
        works = work_items.objects.filter(
            work_item=True).order_by('sort_order', 'id')
        title = 'Edit work items only'
    elif filter == 'shop':
        works = work_items.objects.filter(
            shop_item=True).order_by('sort_order', 'id')
        title = 'Edit Shop items only'
    else:
        works = work_items.objects.all().order_by('sort_order', 'id')
        title = 'Edit all works'
    return render(request, "listworks.html", {'title': title,
                                              'works': works})


@login_required(login_url='accounts:log_in')
@admin_only
def set_works_order(request, pk):
    """
    Delete a work item from the database
    """
    # Check if this work exists
    try:
        work = work_items.objects.get(pk=pk)
    except:
        # if not return to the works list
        return redirect('dashboard:list_works')
    if request.method == 'POST':
        order = request.POST.get("sort_order")
        work.sort_order = order
        work.save()
    return redirect('dashboard:list_works')


@login_required(login_url='accounts:log_in')
@admin_only
def delete_work(request, pk):
    """
    Delete a work item from the database
    """
    # Check if this work exists
    try:
        work = work_items.objects.get(pk=pk)
    except:
        # if not return to the works list
        return redirect('dashboard:list_works')
    # when confirmed delete the image
    if request.method == 'POST':
        work.delete()
        messages.success(request, work.title + 'was successfully deleted')
        return redirect('dashboard:list_works')
    # render confirmation page
    return render(request, "delete_work.html",
                  {'title': 'Permanently delete this work?',
                   'work': work,
                   })


@login_required(login_url='accounts:log_in')
@admin_only
def edit_works(request, pk=None):
    """
    Add a new work-item to the database
    Edit an existing work-item, with optional related shop-item
    Add extra images to the work-item
    """
    # Check if this is an extisting work
    if pk:
        try:
            work = work_items.objects.get(pk=pk)
        except:
            # if not create a new one
            return redirect('dashboard:add_works')
        # if so create asociated forms
        title = 'Edit work details'
        form = EditWorksForm(instance=work)
        image_form = AddExtraImagesForm({'work_item': work.id})
        # check if there are already extra images for this work
        if work_images.objects.filter(work_item=work.id).count() == 0:
            images = None
        else:
            images = work_images.objects.filter(work_item=work.id)
        # Check if this is also a shop item
        if work.shop_item == True:
            # Check if the shop item is already created
            try:
                shop_work = shop_items.objects.get(id=work.shop_settings.id)
                # create form with ixisting settings
                shop_form = EditShopWorksForm(instance=shop_work)
                title = 'Edit work & shop details'
            except:
                # If not create a form with a new shop item
                shop_form = EditShopWorksForm()
                shop_work = None
        else:
            # Set no shop items
            shop_form = None
            shop_work = None
    else:
        # Only create a new work items form
        title = 'Add a new work'
        work = None
        form = EditWorksForm()
        shop_work = None
        shop_form = None
        images = None
        image_form = None
    # Check if a form was submitted
    if request.method == 'POST':
        # Create form objects with submitted data
        form = EditWorksForm(request.POST, request.FILES, instance=work)
        shop_form = EditShopWorksForm(request.POST, instance=shop_work)
        image_form = AddExtraImagesForm(request.POST, request.FILES)
        # Check wich form was submitted and save to database
        if form.is_valid():
            work = form.save()
        if shop_form.is_valid():
            shop_work = shop_form.save()
            # Check if this is the initial shop_settings
            try:
                existing_shop = shop_items.objects.get(
                    id=work.shop_settings.id)
            # if so connect to work
            except:
                work = get_object_or_404(work_items, pk=pk)
                work.shop_settings = shop_work
                work.save()
        if image_form.is_valid():
            new_work_images = image_form.save()
        # Return to edit page for specific work
        return redirect('dashboard:edit_works', work.pk)
    else:
        # Show the edit-work page
        return render(request, "editworks.html", {'title': title,
                                                  'edit_works': form,
                                                  'edit_shop': shop_form,
                                                  'work': work,
                                                  'images': images,
                                                  'add_images': image_form})


@login_required(login_url='accounts:log_in')
@admin_only
def delete_image(request, pk):
    """
    Delete an extra image from the database
    """
    image = get_object_or_404(work_images, pk=pk)
    work = get_object_or_404(work_items, pk=image.work_item.id)
    # when confirmed delete the image
    if request.method == 'POST':
        image.delete()
        return redirect('dashboard:edit_works', work.pk)
    # render confirmation page
    return render(request, "delete_image.html",
                  {'title': 'Permanently delete this image?',
                   'work': work,
                   'image': image})
