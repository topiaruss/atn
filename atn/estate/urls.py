from django.urls import path

from . import views

urlpatterns = [
    path('', views.zone_index, name='zone-index'),
    path('', views.site_index, name='site-index'),
]