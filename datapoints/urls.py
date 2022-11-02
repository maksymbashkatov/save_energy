from django.urls import path
from datapoints.views import DatapointRetrieveAPIView, DatapointUpdateAPIView

urlpatterns = [
    path('<int:pk>', DatapointRetrieveAPIView.as_view()),
    path('change/<int:pk>', DatapointUpdateAPIView.as_view())
]
