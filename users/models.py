from django.contrib.auth.models import AbstractUser
from django.db import models
from organizations.models import OrganizationProject
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    roles = (
        ('A', 'Admin'),
        ('M', 'Moderator'),
        ('S', 'Simple')
    )

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=roles, default=roles[2][0])
    organization_project = models.ForeignKey(OrganizationProject, on_delete=models.CASCADE, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
