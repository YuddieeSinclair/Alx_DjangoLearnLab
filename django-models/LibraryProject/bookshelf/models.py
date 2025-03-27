from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=100, null=False)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}, publication_year: {self.publication_year}"


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(max_length=200)
    profile_photo = models.ImageField


    def __str__(self):
        return f"{CustomUser.date_of_birth}"
    

class UserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, passowrd=None):
        user = self.model(
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )

        user.set_password = passowrd
        user.save(using=self._db)
        return user
    

    def create_superuser(self, date_of_birth, profile_photo, passowrd=None):
        user = self.create_user(
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )
        user.is_admin = True
        user.save(using=self._db)
        return user