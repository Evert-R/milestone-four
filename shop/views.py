from django.shortcuts import render
from works.models import work_items, work_images, categories
from .models import shop_message

# Create your views here.


def all_shop_works(request):
    """
    Show all works in the shop
    """
    # Only show shop message from the navbar link
    info = request.GET.get('info')
    # Get the shop message object
    try:
        message = shop_message.objects.first()
    except:
        message = None
    # Show only if message is set to show
    if message.show == False:
        message = None
    # Get all works for the shop
    works = work_items.objects.filter(
        shop_item=True).order_by('shop_settings__sort_order', 'id')
    return render(request, "shopworks.html", {"works": works,
                                              "message": message,
                                              "info": info})


def shop_details(request, pk):
    next = request.GET.get('next', '/')
    work = work_items.objects.get(pk=pk)
    images = work_images.objects.filter(
        work_item_id=pk).order_by('sort_order', 'id')
    return render(request, "shopdetails.html",
                  {"work": work,
                   "images": images,
                   "next": next})
