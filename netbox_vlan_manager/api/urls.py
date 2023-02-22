from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_vlan_manager'

router = NetBoxRouter()
router.register('vlan-group-sets', views.VLANGroupSetListViewSet)

urlpatterns = router.urls
