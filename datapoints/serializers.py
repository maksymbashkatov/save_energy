from rest_framework import serializers
from datapoints.models import Datapoint


class DatapointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datapoint
        fields = ('name', 'creation_datetime', 'counter_data', 'organization_object')
        read_only_fields = ('creation_datetime',)
