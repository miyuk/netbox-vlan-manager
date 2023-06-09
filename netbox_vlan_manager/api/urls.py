from django.urls import path
from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_vlan_manager'

router = NetBoxRouter()
router.register('vlan-group-sets', views.VLANGroupSetListViewSet)

urlpatterns = [
    path(
        'vlan-group-sets/<int:pk>/available-vlans/',
        views.AvailableVLANsView.as_view(),
        name='vlangroupset-available-vlans'
    ),
]
urlpatterns += router.urls
