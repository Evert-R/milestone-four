from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LogInForm, RegisterForm

# Create your views here.


def register_user(request):
    """Register new users"""
    accounts_form = RegisterForm()
    if request.method == 'POST':
        accounts_form = RegisterForm(request.POST)
        if accounts_form.is_valid():
            user = accounts_form.save()
            username = accounts_form.cleaned_data.get('username')
            messages.success(request, 'You are now registered as ' + username)
            return redirect('works:all_works')
    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Please register here'})


def log_in(request):
    """Show login page"""

    accounts_form = LogInForm()
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

    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Please login here'})


@login_required
def log_out(request):
    """Log out user"""
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('all_works'))
