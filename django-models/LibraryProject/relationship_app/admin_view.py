from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.shortcuts import HttpResponse


def Admin_View(user):
    access = False
    if user.UserProfile.role(name= 'Admin'):
        access = True
    return access



@user_passes_test(Admin_View)

def admin_view(request):
    return HttpResponse("Hello Admin")