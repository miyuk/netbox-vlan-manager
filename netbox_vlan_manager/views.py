from django.db.models import Count
from netbox.views import generic
from ipam.models import VLAN
from . import models, tables, forms
from .tables import VLANGroupSetVLANTable
from django_tables2.export.export import TableExport

class VLANGroupSetView(generic.ObjectView):
    queryset = models.VLANGroupSet.objects.all()

    def get_extra_context(self, request, instance):
        vlan_groups = instance.vlan_groups.all()
        max_vid = max(vlan_groups, key=(lambda x: x.max_vid)).max_vid
        min_vid = min(vlan_groups, key=(lambda x: x.min_vid)).min_vid

        vlan_group_vlans = []
        for vid in range(min_vid, max_vid + 1):
            item = {}
            item['vid'] = vid
            vlans = VLAN.objects.filter(vid=vid)
            item['vlans'] = vlans
            item['status'] = 'Available' if vlans.count() == 0 else 'In Use'
            vlan_group_vlans.append(item)
        vlans_table = VLANGroupSetVLANTable(
            vlan_group_vlans, vlan_groups=vlan_groups)
        vlans_table.configure(request)

        return {
            'vlans_table': vlans_table
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

class VLANGroupSetExportVLANs(generic.ObjectView):
    queryset = models.VLANGroupSet.objects.all()

    def get(self, request, **kwargs):
        print(kwargs)
        instance = self.get_object(**kwargs)
        vlan_groups = instance.vlan_groups.all()
        max_vid = max(vlan_groups, key=(lambda x: x.max_vid)).max_vid
        min_vid = min(vlan_groups, key=(lambda x: x.min_vid)).min_vid

        vlan_group_vlans = []
        for vid in range(min_vid, max_vid + 1):
            item = {}
            item['vid'] = vid
            vlans = VLAN.objects.filter(vid=vid)
            item['vlans'] = vlans
            item['status'] = 'Available' if vlans.count() == 0 else 'In Use'
            vlan_group_vlans.append(item)
        vlans_table = VLANGroupSetVLANTable(
            vlan_group_vlans, vlan_groups=vlan_groups)
        vlans_table.configure(request)
        exporter = TableExport('csv', vlans_table)
        return exporter.response(f'VLANGroupSetVLANs_{instance.name}.csv')