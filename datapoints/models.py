from django.db import models
from organizations.models import OrganizationObject


class Datapoint(models.Model):
    name = models.CharField(max_length=30)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    counter_data = models.IntegerField(blank=True, null=True)
    organization_project = models.ForeignKey(OrganizationObject, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Datapoints'
        verbose_name = 'Datapoint'
        verbose_name_plural = 'Datapoints'
