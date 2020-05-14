from django.shortcuts import render
from works.models import work_items, work_images, categories
from works.forms import FilterForm
import math
# Create your views here.


def all_works(request):
    works = work_items.objects.all()
    filter_form = FilterForm()
    if request.method == "POST":
        filter_method = FilterForm(request.POST)
        if filter_method.is_valid():
            filter_results = filter_method.cleaned_data['cat'].id
            works = work_items.objects.filter(
                category=filter_results)
            return render(request, "works.html", {"works": works, "filter_form": filter_form})
    else:
        works = work_items.objects.all().order_by('sort_order', 'id')
        return render(request, "works.html", {"works": works, "filter_form": filter_form})


def work_details(request, pk):
    """ 
    Display a works details 
    and an overview of all works beneath
    """
    work = work_items.objects.get(pk=pk)
    images = work_images.objects.filter(
        work_item_id=pk).order_by('sort_order', 'id')
    works = work_items.objects.all().order_by('sort_order', 'id')
    return render(request, "workdetails.html", {"work": work,
                                                "images": images,
                                                "works": works, })


def all_test(request):
    return render(request, "test.html")
