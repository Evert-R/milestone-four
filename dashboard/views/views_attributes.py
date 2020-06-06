from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from accounts.decorators import admin_only

from works.models import categories
from shop.models import work_sizes, work_types, materials, shipping


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
