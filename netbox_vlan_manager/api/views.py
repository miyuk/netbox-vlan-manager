from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet
from .serializers import VLANGroupSetSerializer
from ..models import VLANGroupSet


class VLANGroupSetListViewSet(NetBoxModelViewSet):
    queryset = VLANGroupSet.objects.prefetch_related('tags').annotate(
        vlan_group_count=Count('vlan_groups')
    )
    serializer_class = VLANGroupSetSerializer
