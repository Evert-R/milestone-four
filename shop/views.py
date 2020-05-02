from django.shortcuts import render
from works.models import work_items, work_images, categories

# Create your views here.


def all_shop_works(request):
    works = work_items.objects.filter(
        shop_item=True)
    return render(request, "shopworks.html", {"works": works})


def shop_details(request, pk):
    work = work_items.objects.get(pk=pk)
    images = work_images.objects.filter(work_item_id=pk)
    return render(request, "shopdetails.html", {"work": work, "images": images})
