from rest_framework import serializers
from datapoints.models import Datapoint


class DatapointSerializer(serializers.ModelSerializer):
    # organization_object_name = serializers.CharField()
    # organization_project_name = serializers.CharField()

    class Meta:
        model = Datapoint
        fields = ('name', 'creation_datetime', 'counter_data', 'organization_object')
        read_only_fields = ('creation_datetime',)
