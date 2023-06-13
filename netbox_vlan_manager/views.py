from django.db.models import Count
from django_tables2.export.export import TableExport
from netbox.views import generic
from ipam.models import VLAN
from .models import VLANGroupSet
from .forms import VLANGroupSetForm
from .tables import VLANGroupSetVLANTable, VLANGroupSetTable


class VLANGroupSetView(generic.ObjectView):
    queryset = VLANGroupSet.objects.all()

    def get_extra_context(self, request, instance):
        show_available = bool(request.GET.get('show_available', 'true') == 'true')
        show_assigned = bool(request.GET.get('show_assigned', 'true') == 'true')
        vlan_groups = instance.vlan_groups.all()
        vlan_group_vlans = instance.vlans
        requested_vlans = [
            x for x in vlan_group_vlans
            if show_available and x['status'] == 'Available' or show_assigned and x['status'] == 'Assigned'
        ]
        vlans_table = VLANGroupSetVLANTable(requested_vlans, vlan_groups=vlan_groups)
        vlans_table.configure(request)

        return {
            'vlans_table': vlans_table,
            'show_available': show_available,
            'show_assigned': show_assigned,
        }


class VLANGroupSetListView(generic.ObjectListView):
    queryset = VLANGroupSet.objects.annotate(
        vlan_group_count=Count('vlan_groups')
    )
    table = VLANGroupSetTable


class VLANGroupSetEditView(generic.ObjectEditView):
    queryset = VLANGroupSet.objects.all()
    form = VLANGroupSetForm


class VLANGroupSetDeleteView(generic.ObjectDeleteView):
    queryset = VLANGroupSet.objects.all()


class VLANGroupSetExportVLANs(generic.ObjectView):
    queryset = VLANGroupSet.objects.all()

    def get(self, request, **kwargs):
        instance = self.get_object(**kwargs)
        vlan_groups = instance.vlan_groups.all()
        vlan_group_vlans = instance.vlans
        vlans_table = VLANGroupSetVLANTable(
            vlan_group_vlans, vlan_groups=vlan_groups)
        vlans_table.configure(request)

        vlans_table = VLANGroupSetVLANTable(
            vlan_group_vlans, vlan_groups=vlan_groups)
        vlans_table.configure(request)
        exporter = TableExport('csv', vlans_table)
        return exporter.response(f'VLANGroupSetVLANs_{instance.name}.csv')
