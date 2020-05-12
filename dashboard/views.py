from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from works.models import work_items, categories, work_images
from shop.models import shop_items, work_sizes, work_types, materials, shipping
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
        filter = 'all'
    return render(request, "listworks.html", {'title': title,
                                              'works': works,
                                              'filter': filter})


@login_required(login_url='accounts:log_in')
@admin_only
def set_works_order(request, pk):
    """
    Set the display order for works
    """

    # Check if this work exists
    try:
        work = work_items.objects.get(pk=pk)
    except:
        # if not return to the works list
        return redirect('dashboard:list_works')
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        order = request.POST.get("sort_order")
        work.sort_order = order
        work.save()
    return redirect(next)


@login_required(login_url='accounts:log_in')
@admin_only
def set_shop_order(request, pk):
    """
    Set the display order for shop items
    """

    # Check if this work exists
    try:
        work = work_items.objects.get(pk=pk)
    except:
        # if not return to the works list
        return redirect('dashboard:list_works')
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        order = request.POST.get("sort_order")
        work.shop_settings.sort_order = order
        work.shop_settings.save()
    return redirect(next)


@login_required(login_url='accounts:log_in')
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
        return redirect('dashboard:list_works')
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        order = request.POST.get("sort_order")
        image.sort_order = order
        image.save()
    return redirect(next)


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
            images = work_images.objects.filter(
                work_item=work.id).order_by('sort_order', 'id')
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
        cats = categories.objects.all()
        sizes = work_sizes.objects.all()
        mats = materials.objects.all()
        sizes = work_sizes.objects.all()
        types = work_types.objects.all()
        # Show the edit-work page
        return render(request, "editworks.html", {'title': title,
                                                  'edit_works': form,
                                                  'edit_shop': shop_form,
                                                  'work': work,
                                                  'images': images,
                                                  'add_images': image_form,
                                                  'categories': cats,
                                                  'sizes': sizes,
                                                  'materials': mats,
                                                  'sizes': sizes,
                                                  'types': types})


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


@login_required()
@admin_only
def edit_categories(request, pk=None):
    # if this is an extisting category
    if pk:
        # Get the category
        try:
            category = categories.objects.get(pk=pk)
        # When not found return to origin
        except:
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('category')
            category.name = new_name
            category.save()
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            category.delete()
            return redirect(next)
    # if not an extisting category
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('category')
            new_category = categories(name=new_name)
            new_category.save()
        return redirect(next)


@login_required()
@admin_only
def edit_work_types(request, pk=None):
    # if this is an extisting work type
    if pk:
        # Get the work type
        try:
            work_type = work_types.objects.get(pk=pk)
        # When not found return to origin
        except:
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the work type name
            new_name = request.POST.get('worktype')
            work_type.name = new_name
            work_type.save()
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            work_type.delete()
            return redirect(next)
    # if not an extisting work type
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('worktype')
            new_work_type = work_types(name=new_name)
            new_work_type.save()
        return redirect(next)


@login_required()
@admin_only
def edit_work_sizes(request, pk=None):
    # if this is an extisting category
    if pk:
        # Get the category
        try:
            work_size = work_sizes.objects.get(pk=pk)
        # When not found return to origin
        except:
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('worksize')
            work_size.name = new_name
            work_size.save()
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            work_size.delete()
            return redirect(next)
    # if not an extisting category
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('worksize')
            new_work_size = work_sizes(name=new_name)
            new_work_size.save()
        return redirect(next)


@login_required()
@admin_only
def edit_materials(request, pk=None):
    # if this is an extisting material
    if pk:
        # Get the material
        try:
            material = materials.objects.get(pk=pk)
        # When not found return to origin
        except:
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('material')
            material.name = new_name
            material.save()
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            material.delete()
            return redirect(next)
    # if not an extisting material
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('material')
            new_material = materials(name=new_name)
            new_material.save()
        return redirect(next)


@login_required()
@admin_only
def edit_settings(request):
    shippings = shipping.objects.all()
    title = 'Adjust shop settings'
    return render(request, "settings.html", {'title': title,
                                             'shippings': shippings})


@login_required()
@admin_only
def edit_shipping(request, pk=None):
    # if this is an extisting region
    if pk:
        # Get the region
        try:
            this_shipping = shipping.objects.get(pk=pk)
        # When not found return to origin
        except:
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the region
            new_region = request.POST.get('region')
            new_price = request.POST.get('price')
            this_shipping.region = new_region
            this_shipping.price = new_price
            this_shipping.save()
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            this_shipping.delete()
            return redirect(next)
    # if not an extisting region
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_region = request.POST.get('region')
            new_price = request.POST.get('price')
            new_shipping = shipping(region=new_region, price=new_price)
            new_shipping.save()
        return redirect(next)
