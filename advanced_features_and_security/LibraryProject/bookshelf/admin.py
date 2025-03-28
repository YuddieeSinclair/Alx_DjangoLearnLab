from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


class CustomUserAdmin(BaseAdmin):
    list_display = ('date_of_birth', 'profile_photo')
    search_fields = ('date_of_birth')
    list_filter = ("is_admin")

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)