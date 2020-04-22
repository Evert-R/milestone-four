from django.shortcuts import render, get_object_or_404, redirect
from works.models import work_items, categories
from shop.models import shop_items, work_sizes, work_types, materials
from dashboard.forms import EditWorksForm, EditShopWorksForm

# Create your views here.


def edit_works(request, pk=None):
    """
    Add a new work-item to the database
    Edit an existing work-item, with optional related shop-item    
    """
    # Check if this is an extisting work
    if pk:
        work = get_object_or_404(work_items, pk=pk)
        form = EditWorksForm(instance=work)
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
    # Check if a form was submitted
    if request.method == 'POST':
        # Create a form instance with submitted data
        form = EditWorksForm(request.POST, request.FILES, instance=work)
        shop_form = EditShopWorksForm(request.POST, instance=shop_work)
        # Check wich form was submitted and save
        if form.is_valid():
            work = form.save()
        if shop_form.is_valid():
            shop_work = shop_form.save()
        return redirect('dashboard:edit_works', work.pk)
    else:
        # if a shop-item form was made then render it
        if shop_form:
            return render(request, "editworks.html", {'edit_works': form, 'edit_shop': shop_form})
        # only render work-item form
        else:
            return render(request, "editworks.html", {'edit_works': form})
