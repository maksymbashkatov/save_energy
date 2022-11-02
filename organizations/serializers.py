from rest_framework import serializers
from organizations.models import OrganizationProject, OrganizationObject


class OrganizationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProject
        fields = ('name',)


class OrganizationObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationObject
        fields = ('name', 'organization_project')
