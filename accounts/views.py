from django.shortcuts import render, redirect, reverse,  get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from accounts.models import user_details
from accounts.forms import LogInForm, RegisterForm, UserDetailsForm
from accounts import decorators

# Create your views here.


def register_user(request):
    """Register new users"""

    accounts_form = RegisterForm()
    # check if a form was submitted
    if request.method == 'POST':
        # Create form object with submitted data
        accounts_form = RegisterForm(request.POST)
        if accounts_form.is_valid():
            # when valid save user to the database
            user = accounts_form.save()
            username = accounts_form.cleaned_data.get('username')
            # Add user to the customer group
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # Display success message
            messages.success(request, 'You are now registered as ' + username)
            # Redirect to the shop page
            return redirect('works:all_works')
    # Show the register page
    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Please register here'})


def add_user_details(request, next_page):
    """Add or edit user details"""

    active_user = request.user
    if user_details.objects.filter(user=active_user.id).count() == 0:
        accounts_form = UserDetailsForm({'user': active_user.id})
        current_user_details = None
    else:
        current_user_details = get_object_or_404(user_details,
                                                 user=active_user.id)
        accounts_form = UserDetailsForm(instance=current_user_details)

    if request.method == 'POST':
        accounts_form = UserDetailsForm(
            request.POST, instance=current_user_details)
        if accounts_form.is_valid():
            current_user_details = accounts_form.save()
            messages.success(request, 'Your details have been saved')
            return redirect(next_page)
    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Shipping details'})


def log_in(request):
    """Show login page"""
    accounts_form = LogInForm()
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in !')
        return redirect(reverse('all_works'))
    # check if a form was submitted
    if request.method == 'POST':
        # Create form object with submitted data
        accounts_form = LogInForm(request.POST)

        if accounts_form.is_valid():
            # when valid authenticate the user
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user is not None:
                # When a user is matched log in
                auth.login(user=user, request=request)
                # Display success message
                messages.success(request, "You are now logged in!")
                # redirect user to the shop page
                next = request.POST.get('next', '/')
                return redirect(next)
            else:
                # When user was not matched return the form with errors
                accounts_form.add_error(
                    None, "Your username or password is incorrect")
    # Show the login page
    return render(request, 'accounts.html', {'accounts_form': accounts_form, 'form_title': 'Please login here'})


@login_required
def log_out(request):
    """Log out user"""

    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('all_works'))
