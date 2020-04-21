from django.shortcuts import render, get_object_or_404, redirect
from works.models import work_items, categories
from dashboard.forms import EditWorksForm

# Create your views here.


def edit_works(request, pk=None):
    work = get_object_or_404(work_items, pk=pk) if pk else None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditWorksForm(request.POST, request.FILES, instance=work)
        # check whether it's valid:
        if form.is_valid():
            work = form.save()
            return redirect('dashboard:edit_works', work.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditWorksForm(instance=work)
    return render(request, "EditWorksForm.html", {'edit_works': form})
