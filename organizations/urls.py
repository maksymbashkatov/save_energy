from django.urls import path
from organizations.views import OrganizationProjectListAPIView, OrganizationObjectListAPIView

urlpatterns = (
    path('projects', OrganizationProjectListAPIView.as_view()),
    path('objects', OrganizationObjectListAPIView.as_view())
)
