from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from datapoints.models import Datapoint
from datapoints.serializers import DatapointSerializer


class DatapointRetrieveAPIView(RetrieveAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (IsAuthenticated,)


class DatapointUpdateAPIView(UpdateAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        print(request)
        return self.update(request, *args, **kwargs)
