from django.shortcuts import redirect
from django.contrib import auth, messages


def admin_only(view_func):
    """Check if user is the admin"""

    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            messages.error(request, 'You are not allowed to view that page')
            return redirect('works:all_works')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
