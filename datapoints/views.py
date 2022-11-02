from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from datapoints.models import Datapoint
from datapoints.serializers import DatapointSerializer


class DatapointRetrieveAPIView(RetrieveAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (IsAuthenticated,)
