from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    roles = (
        ('A', 'admin'),
        ('M', 'moderator'),
        ('SU', 'simple_user')
    )

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=roles, default=roles[2][0])
    organization_project = ...

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'
