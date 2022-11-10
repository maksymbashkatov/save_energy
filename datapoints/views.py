from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from datapoints.models import Datapoint
from datapoints.serializers import DatapointSerializer


class DatapointViewSet(RetrieveModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def counter_data(self, request, pk=None):
        qp = request.query_params
        qs = self.queryset
        if qp:
            if 'month' in qp:
                return Response(qs.filter(creation_datetime__month=qp['month']).aggregate(avg_month=Avg('counter_data')))
            elif 'day' in qp:
                return Response(qs.filter(creation_datetime__day=qp['day']).aggregate(avg_day=Avg('counter_data')))
            elif 'hour' in qp:
                return Response(qs.filter(creation_datetime__hour=qp['hour']).aggregate(avg_hour=Avg('counter_data')))
        else:
            return Response({'counter_data': qs.get(pk=pk).counter_data})
