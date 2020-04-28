from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from works.models import work_items, categories, work_images
from shop.models import shop_items, work_sizes, work_types, materials

from dashboard.forms import EditWorksForm, EditShopWorksForm, AddExtraImagesForm
from accounts.decorators import admin_only

# Create your views here.


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
        # if so create asociated forms
        work = get_object_or_404(work_items, pk=pk)
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
            if shop_items.objects.filter(work_item=work.id).count() == 0:
                # If not create a form with a new shop item
                shop_form = EditShopWorksForm({'work_item': work.id})
                shop_work = None
            else:
                # Create a form with existing shop item
                shop_work = get_object_or_404(shop_items, work_item=work.id)
                shop_form = EditShopWorksForm(instance=shop_work)
        else:
            # Set no shop items
            shop_form = None
            shop_work = None
    else:
        # Only create a new work items form
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
        if image_form.is_valid():
            new_work_images = image_form.save()
        return redirect('dashboard:edit_works', work.pk)
    else:
        # Show the edit-work page
        return render(request, "editworks.html", {'edit_works': form, 'edit_shop': shop_form, 'work': work, 'images': images, 'add_images': image_form})


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
    return render(request, "delete_image.html", {'work': work, 'image': image})
