from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.Author

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=300)
    library = models.OneToOneField(Library, on_delete= models.PROTECT)

    def __str__(self):
        return self.title



from django.contrib.auth.models import User

class UserProfile(models.Model):
    roles = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    role = models.CharField(max_length=10, choices=roles, default="Member")


    def __str__(self):
        return f"{self.user.username} - {self.role}"
    



from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only create profile when a new user is registered
        UserProfile.objects.create(user=instance, role="Member")



@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()