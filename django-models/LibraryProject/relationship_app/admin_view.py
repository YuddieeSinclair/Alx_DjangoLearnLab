from django.contrib.auth.decorators import user_passes_test
from .models import user
from django.shortcuts import HttpResponse


def Admin_View(user):
    return user.role.filter(name= 'Admin')



@user_passes_test(Admin_View)

def admin_dashboard(request):
    return HttpResponse("Hello Admin")