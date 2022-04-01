from locale import normalize
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manages for User Profile"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Not a valid email address")

        email = self.normalize_email("email")
        User = self.model(email = email, name = name)

        User.set_password(password)
        User.save(using = self._db)

        return User

    def create_superuser(self, email, name, password):
        """Create and save superuser with given details"""

        User = self.create_user(email, name, password)

        User.is_superuser = True
        User.is_staff = True
        User.save(using=self._db)

        return User



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the Users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """get full name of the user"""
        return self.name
    
    def get_short_name(self):
        """get short name of the user"""
        return self.name

    def __str__(self):
        """Returns string representation of the user"""
        return self.email