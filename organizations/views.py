from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from organizations.models import OrganizationProject, OrganizationObject
from organizations.serializers import OrganizationProjectSerializer, OrganizationObjectSerializer


class OrganizationProjectListAPIView(ListAPIView):
    serializer_class = OrganizationProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'A':
            return OrganizationProject.objects.all()
        elif user.role == 'M':
            return OrganizationProject.objects.get(pk=user.organization_project.pk)
        else:
            return Response({'role_info': 'You do not have access.'})


class OrganizationObjectListAPIView(ListAPIView):
    serializer_class = OrganizationObjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'S':
            return OrganizationObject.objects.filter(organization_project=user.organization_project)[:1]
        if user.role == 'M':
            return OrganizationObject.objects.filter(organization_project=user.organization_project)
        else:
            return OrganizationObject.objects.all()
