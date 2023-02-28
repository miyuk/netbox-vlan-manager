from django.db.models import Count
from netbox.views import generic
from . import models, tables, forms
from ipam.models import VLAN
from ipam.utils import add_available_vlans
from ipam.tables import VLANTable


class VLANGroupSetView(generic.ObjectView):
    queryset = models.VLANGroupSet.objects.all()

    def get_extra_context(self, request, instance):
        vlan_groups = instance.vlan_groups.all()
        max_vid = max(vlan_groups, key=(lambda x: x.max_vid)).max_vid
        min_vid = min(vlan_groups, key=(lambda x: x.min_vid)).min_vid

        vlan_group_vlans = {}
        for vid in range(min_vid, max_vid + 1):
            vlan_group_vlans[vid] = {}
            for vlan_group in vlan_groups:
                vlans = VLAN.objects.filter(group=vlan_group, vid=vid)
                vlan_group_vlans[vid][vlan_group.id] = vlans[0] if vlans else None

        return {
            'vlan_group_vlans': vlan_group_vlans
        }


class VLANGroupSetListView(generic.ObjectListView):
    queryset = models.VLANGroupSet.objects.annotate(
        vlan_group_count=Count('vlan_groups')
    )
    table = tables.VLANGroupSetTable


class VLANGroupSetEditView(generic.ObjectEditView):
    queryset = models.VLANGroupSet.objects.all()
    form = forms.VLANGroupSetForm


class VLANGroupSetDeleteView(generic.ObjectDeleteView):
    queryset = models.VLANGroupSet.objects.all()
