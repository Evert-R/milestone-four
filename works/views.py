from django.shortcuts import render

# Create your views here.


def all_works(request):
    return render(request, "works.html")


def all_test(request):
    return render(request, "test.html")
