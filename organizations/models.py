from django.db import models


class OrganizationProject(models.Model):
    class Meta:
        db_table = 'OrganizationProjects'
        verbose_name = 'OrganizationProject'
        verbose_name_plural = 'OrganizationProjects'
