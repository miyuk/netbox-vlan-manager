from django.urls import reverse
import django_tables2 as tables
from netbox.tables import NetBoxTable, BaseTable
from .models import VLANGroupSet

VLAN_STATUS = """
{% if record.status == 'Available' %}
    <span class="badge bg-success">{{ record.status }}</span>
{% else %}
    <span class="badge bg-danger">{{ record.status }}</span>
{% endif %}
"""

VLAN_DATA = """
{% load view_helpers %}
{% with vlan=record|get_vlan_by_group:vlan_group %}
    {% if vlan %}
        <a href="{{ vlan.get_absolute_url }}">
            {{ vlan.name }}
        </a>
    {% else %}
        <a href="{% url 'ipam:vlan_add' %}?vid={{ vlan.vid }}&group={{ vlan_group.id }}" class="btn btn-sm btn-success">
            Add VLAN
        </a>
    {% endif %}
{% endwith %}
"""


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


class VLANGroupSetVLANTable(BaseTable):
    vid = tables.Column(
        verbose_name='VID',
        linkify=lambda record: f'{reverse("ipam:vlan_list")}?vid={record["vid"]}'
    )
    status = tables.TemplateColumn(template_code=VLAN_STATUS)

    class Meta(BaseTable.Meta):
        template_name = 'netbox_vlan_manager/vlangroupset_vlans.html'
        empty_text = 'No VLANs found'
        fields = (
            'vid',
            'status',
        )
        row_attrs = {
            'class': lambda record: 'success' if record['status'] == 'Available' else '',
        }

    def __init__(self, *args, vlan_groups=None, **kwargs):
        if vlan_groups is None:
            vlan_groups = []

        self.Meta.fields = list(self.Meta.fields)
        extra_columns = []
        for vlan_group in vlan_groups:
            column_name = f'vlangroup_{vlan_group.id}'
            column = (
                column_name,
                tables.TemplateColumn(
                    verbose_name=f'{vlan_group.name}',
                    template_code=VLAN_DATA,
                    extra_context={'vlan_group': vlan_group},
                )
            )
            extra_columns.append(column)
            # TODO: There's probably a more clever way to accomplish this
            if column_name not in self.Meta.fields:
                self.Meta.fields.append(column_name)

        super().__init__(*args, extra_columns=extra_columns, **kwargs)
