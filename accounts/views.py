from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LogInForm

# Create your views here.


def log_in(request):
    """Show login page"""
    if request.user.is_authenticated:
        return redirect(reverse('all_works'))
    if request.method == 'POST':
        accounts_form = LogInForm(request.POST)

        if accounts_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You are now logged in!")

            if user is not None:
                auth.login(user=user, request=request)
                return redirect(reverse('all_works'))
            else:
                accounts_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        accounts_form = LogInForm()
    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Please login here'})


@login_required
def log_out(request):
    """Log out user"""
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('all_works'))
