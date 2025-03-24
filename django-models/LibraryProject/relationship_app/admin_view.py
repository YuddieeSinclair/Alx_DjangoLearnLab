from .models import UserProfile
from django.shortcuts import HttpResponse


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'