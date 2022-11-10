from rest_framework import routers
from datapoints.views import DatapointViewSet


router_datapoints = routers.SimpleRouter()
router_datapoints.register('', DatapointViewSet)
print(router_datapoints.urls)
