from django.contrib import admin
from django.urls import path, include
from datapoints.urls import router_datapoints


urlpatterns = (
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('datapoints/', include(router_datapoints.urls)),
    path('organizations/', include('organizations.urls'))
)
