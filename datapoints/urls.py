from django.urls import path
from datapoints.views import DatapointRetrieveAPIView, DatapointUpdateAPIView, DatapointListAPIView

urlpatterns = [
    path('<int:pk>', DatapointRetrieveAPIView.as_view()),
    path('change/<int:pk>', DatapointUpdateAPIView.as_view()),
    path('all', DatapointListAPIView.as_view())
]
