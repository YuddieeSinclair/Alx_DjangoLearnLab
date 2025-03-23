from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.shortcuts import HttpResponse
from .decorators import *


@user_passes_test(is_librarian)

def admin_view(request):
    return HttpResponse("Hello librarian")