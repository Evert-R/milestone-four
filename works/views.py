from django.shortcuts import render
from works.models import work_items, categories
from works.forms import FilterForm
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
        works = work_items.objects.all()
        return render(request, "works.html", {"works": works, "filter_form": filter_form})


def work_details(request, pk):
    work = work_items.objects.get(pk=pk)
    return render(request, "workdetails.html", {"work": work})


def all_test(request):
    return render(request, "test.html")
