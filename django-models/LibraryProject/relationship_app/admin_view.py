from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def Admin(request):
    if not is_admin(request.user):
        return PermissionError
    return HttpResponse("welcome admin")
