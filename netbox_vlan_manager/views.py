from django.db.models import Count
from netbox.views import generic
from . import models, tables, forms


class VLANGroupSetView(generic.ObjectView):
    queryset = models.VLANGroupSet.objects.all()


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
