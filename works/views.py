from django.shortcuts import render
from works.models import work_items

# Create your views here.


def all_works(request):
    works = work_items.objects.all()
    return render(request, "works.html", {"works": works})


def all_test(request):
    return render(request, "test.html")
