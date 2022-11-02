from django.urls import path
from datapoints.views import DatapointRetrieveAPIView

urlpatterns = [
    path('<int:pk>', DatapointRetrieveAPIView.as_view())
]
