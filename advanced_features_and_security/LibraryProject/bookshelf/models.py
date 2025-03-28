from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=100, null=False)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}, publication_year: {self.publication_year}"
    

from django.contrib.auth.models import UserManager, BaseUserManager, AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank= True)
    profile_photo = models.ImageField(null=True, blank=True)




class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, password=None):
        new_user = self.model(
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user
    

    def create_superuser(self, date_of_birth, profile_photo, password=None):
        super_user = self.create_user(
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )

        super_user.is_admin = True
        super_user.save(using= self._db)
        return super_user
