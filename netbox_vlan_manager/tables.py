import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import VLANGroupSet


class VLANGroupSetTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    vlan_group_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = VLANGroupSet
        fields = (
            'pk',
            'id',
            'name',
            'vlan_group_count',
            'description',
            'comments'
        )
        default_columns = (
            'name',
            'vlan_group_count',
            'description'
        )
