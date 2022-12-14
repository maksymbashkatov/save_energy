from django.db import models


class OrganizationProject(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'OrganizationProjects'
        verbose_name = 'OrganizationProject'
        verbose_name_plural = 'OrganizationProjects'


class OrganizationObject(models.Model):
    name = models.CharField(max_length=30)
    organization_project = models.ForeignKey(OrganizationProject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrganizationObjects'
        verbose_name = 'OrganizationObject'
        verbose_name_plural = 'OrganizationObjects'
