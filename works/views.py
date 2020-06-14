from django.shortcuts import render
from works.models import work_items, work_images, categories
from works.forms import FilterForm
import math
# Create your views here.


def all_works(request):
    works = work_items.objects.filter(
        work_item=True).order_by('sort_order', 'id')
    filter_form = FilterForm()
    if request.method == "POST":
        filter_method = FilterForm(request.POST)
        if filter_method.is_valid():
            try:
                filter_results = filter_method.cleaned_data['cat'].id
            except:
                return render(request, "works.html", {"works": works,
                                                      "filter_form": filter_form})
            # Set this category as initial value for the form
            filter_form.fields['cat'].initial = filter_results
            works = works.filter(
                category=filter_results)
            return render(request, "works.html", {"works": works,
                                                  "filter_form": filter_form})
    else:
        return render(request, "works.html", {"works": works,
                                              "filter_form": filter_form})


def work_details(request, pk):
    """ 
    Display a works details 
    and an overview of all works beneath
    """
    next = request.GET.get('next', '/')
    work = work_items.objects.get(pk=pk)
    images = work_images.objects.filter(
        work_item_id=pk).order_by('sort_order', 'id')
    works = work_items.objects.filter(
        work_item=True).order_by('sort_order', 'id')
    if work.collection == True:
        return render(request, "collection.html", {"work": work,
                                                   "images": images,
                                                   "works": works,
                                                   "next": next})
    else:
        return render(request, "workdetails.html", {"work": work,
                                                    "images": images,
                                                    "works": works,
                                                    "next": next})
