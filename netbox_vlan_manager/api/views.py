from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from netbox.config import get_config
from netbox.api.viewsets import NetBoxModelViewSet
from .serializers import VLANGroupSetSerializer, AvailableVLANSerializer
from ..models import VLANGroupSet


def get_results_limit(request):
    config = get_config()
    try:
        limit = int(request.query_params.get(
            'limit', config.PAGINATE_COUNT)) or config.MAX_PAGE_SIZE
    except ValueError:
        limit = config.PAGINATE_COUNT
    if config.MAX_PAGE_SIZE:
        limit = min(limit, config.MAX_PAGE_SIZE)

    return limit


class VLANGroupSetListViewSet(NetBoxModelViewSet):
    queryset = VLANGroupSet.objects.prefetch_related('tags').annotate(
        vlan_group_count=Count('vlan_groups')
    )
    serializer_class = VLANGroupSetSerializer


class AvailableVLANsView(APIView):
    queryset = VLANGroupSet.objects

    def get(self, request, pk):
        vlan_group_set = get_object_or_404(VLANGroupSet, pk=pk)
        limit = get_results_limit(request)

        available_vlans = vlan_group_set.get_available_vids()[:limit]
        serializer = AvailableVLANSerializer(available_vlans, many=True, context={
            'request': request,
            'group_set': vlan_group_set,
        })

        return Response(serializer.data)
