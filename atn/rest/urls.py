from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'zones', views.ZoneViewSet)
router.register(r'sites', views.SiteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('sites_by_zone/<int:zone_id>', views.SiteByZoneList.as_view(), name='sites-by-zone'),
]