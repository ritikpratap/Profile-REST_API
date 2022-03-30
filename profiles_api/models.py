from locale import normalize
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manages for User Profile"""

    def create_user(self, Email, Name, Password=None):
        if not Email:
            raise ValueError("Not a valid email address")

        Email = self.normalize_email("Email")
        User = self.model(Email = Email, Name = Name)

        User.set_password(Password)
        User.save(using = self._db)

        return User

    def create_superuser(self, Email, Name, Password):
        """Create and save superuser with given details"""

        User = self.create_user(Email, Name, Password)

        User.is_superuser = True
        User.is_staff = True
        User.save(using=self._db)

        return User



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the Users in the system"""

    Email = models.EmailField(max_length=255, unique=True)
    Name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "Email"
    REQUIRED_FIELDS = ["Name"]

    def get_full_name(self):
        """get full name of the user"""
        return self.Name
    
    def get_short_name(self):
        """get short name of the user"""
        return self.Name

    def __str__(self):
        """Returns string representation of the user"""
        return self.Email