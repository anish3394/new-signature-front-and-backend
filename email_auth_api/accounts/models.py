from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()
