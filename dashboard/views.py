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
    Display a list of all orders
    With links to their details pages
    """

    # Get all orders
    all_orders = orders.objects.all()
    title = 'Viewing all orders'
    return render(request, "listorders.html",
                  {'title': title,
                   'orders': all_orders})


@login_required(login_url='accounts:log_in')
@admin_only
def view_order(request, pk):
    """
    Display the details of an order
    With buttons to update shipping/ payment status
    """
    # Check if this order exists
    try:
        order = orders.objects.get(pk=pk)
    # if not show the list and rais an error message
    except:
        messages.error(request,
                       'This order does not exist')
        return redirect('dashboard:list_orders')
    # Check if there are order items
    try:
        items = order_items.objects.filter(order=order)
    # If not show the list and raise an error message
    except:
        messages.error(request,
                       'This order does not have any items')
        return redirect('dashboard:list_orders')
    title = 'Viewing order'
    return render(request, "vieworder.html", {'title': title,
                                              'order': order,
                                              'items': items})


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


@login_required(login_url='accounts:log_in')
@admin_only
def list_works(request, filter=None):
    """
    Display a list of all works
    With links to their edit pages
    Change display order of works
    """

    # Check wich filter was selected and get objects
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
    Set the display order for work view
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
        work.sort_order = order
        work.save()
        messages.success(request, 'Display order of ' +
                         work.title + ' has been updated')
    return redirect(next)


@login_required(login_url='accounts:log_in')
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
        messages.error(request,
                       'This work does not exist')
        return redirect('dashboard:list_works')
    # when confirmed delete the image
    if request.method == 'POST':
        # Delete image from filesystem
        work.main_image.delete()
        # Delete work object
        work.delete()
        messages.success(request,
                         work.title
                         + ' was successfully deleted')
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
            messages.success(request,
                             work.title + ' has been saved')
        if shop_form.is_valid():
            shop_work = shop_form.save()
            messages.success(request,
                             'Shop settings have been updated')
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
            messages.success(request,
                             'Image has been added to '
                             + work.title)
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
    try:
        image = work_images.objects.get(pk=pk)
    except:
        messages.error(request,
                       'This image does not exist')
        return redirect('dashboard:list_works')
    try:
        work = work_items.objects.get(pk=image.work_item.id)
    except:
        messages.error(request,
                       'This image does not belong to an existing work')
        return redirect('dashboard:list_works')
    # when confirmed delete the image and remove object
    if request.method == 'POST':
        image.work_image.delete()
        image.delete()
        messages.success(request,
                         'The image was successfully deleted')
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
            messages.error(request,
                           'This category does not exist')
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('category')
            category.name = new_name
            category.save()
            messages.success(
                request, 'Category has been changed to '
                + category.name)
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, category.name
                             + ' has been deleted')
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
            messages.success(request, new_category.name
                             + ' has been saved')
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
            messages.error(request,
                           'This work type does not exist')
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the work type name
            new_name = request.POST.get('worktype')
            work_type.name = new_name
            work_type.save()
            messages.success(request,
                             'Work type had been changed to '
                             + work_type.name)
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, work_type.name
                             + ' had been deleted')
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
            messages.success(request, new_work_type.name
                             + ' has been saved')
        return redirect(next)


@login_required()
@admin_only
def edit_work_sizes(request, pk=None):
    # if this is an extisting work-size
    if pk:
        # Get the category
        try:
            work_size = work_sizes.objects.get(pk=pk)
        # When not found return to origin
        except:
            messages.error(request,
                           'This work size does not exist')
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('worksize')
            work_size.name = new_name
            work_size.save()
            messages.success(
                request, 'Work size had been changed to '
                + work_size.name)
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, work_size.name
                             + ' had been deleted')
            work_size.delete()
            return redirect(next)
    # if not an extisting work-size
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('worksize')
            new_work_size = work_sizes(name=new_name)
            new_work_size.save()
            messages.success(request, new_work_size.name
                             + ' has been saved')
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
            messages.error(request,
                           'This material does not exist')
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('material')
            material.name = new_name
            material.save()
            messages.success(
                request, 'Material has been changed to '
                + material.name)
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, material.name
                             + ' has been deleted')
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
            messages.success(request, new_material.name
                             + ' has been saved')
        return redirect(next)


@login_required()
@admin_only
def edit_settings(request):
    """
    Edit shop settings
    """

    shippings = shipping.objects.all()
    title = 'Adjust shop settings'
    return render(request, "settings.html",
                  {'title': title,
                   'shippings': shippings})


@login_required()
@admin_only
def edit_shipping(request, pk=None):
    """
    Add/edit shipping region/costs
    """

    # if this is an extisting region
    if pk:
        # Get the region
        try:
            this_shipping = shipping.objects.get(pk=pk)
        # When not found return to origin
        except:
            messages.error(request,
                           'This region does not exist')
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
            messages.success(request, this_shipping.region +
                             ' was changed to '
                             + this_shipping.price
                             + ' Euro')
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, this_shipping.region +
                             ' has been deleted')
            this_shipping.delete()
            return redirect(next)
    # if not an extisting region
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_region = request.POST.get('region')
            new_price = request.POST.get('price')
            new_shipping = shipping(region=new_region,
                                    price=new_price)
            new_shipping.save()
            messages.success(request,
                             new_shipping.region
                             + ' has been saved')
        return redirect(next)
