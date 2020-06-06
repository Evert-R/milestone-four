from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from accounts.decorators import admin_only

# Create your views here.


@login_required()
@admin_only
def edit_clients(request, pk=None):
    # if this is an extisting category
    if pk:
        # Get the category
        try:
            client = clients.objects.get(pk=pk)
        # When not found return to origin
        except:
            messages.error(request,
                           'This client does not exist')
            return redirect(next)
        # if a form was posted
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            # Update the category name
            new_name = request.POST.get('client')
            client.name = new_name
            client.save()
            messages.success(
                request, 'Client has been changed to '
                + category.name)
            return redirect(next)
        # If not delete it
        else:
            next = request.GET.get('next', '/')
            messages.success(request, client.name
                             + ' has been deleted')
            client.delete()
            return redirect(next)
    # if not an extisting category
    else:
        # Create a new one
        if request.method == 'POST':
            next = request.POST.get('next', '/')
            new_name = request.POST.get('client')
            new_client = clients(name=new_name)
            new_client.save()
            messages.success(request, new_client.name
                             + ' has been saved')
        return redirect(next)
