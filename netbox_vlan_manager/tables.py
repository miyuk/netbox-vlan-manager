import django_tables2 as tables
from netbox.tables import NetBoxTable, BaseTable
from .models import VLANGroupSet


VLAN_LINK = """
<a href="{% url 'ipam:vlan_list' %}?vid={{ record.vid }}">{{ record.vid }}</a>
"""

VLAN_VLANS = """
{% if record.vlans %}
    {% for vlan in record.vlans %}
    {{ vlan.name }}({{ vlan.status }})
    {% endfor %}
{% else %}
    <span class="badge bg-success">Available VLAN</span>
{% endif %}
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
    vid = tables.TemplateColumn(
        template_code=VLAN_LINK, orderable=True, verbose_name='VID')
    vlans = tables.TemplateColumn(
        template_code=VLAN_VLANS, orderable=True, verbose_name='VLANs')

    class Meta(BaseTable.Meta):
        empty_text = 'No VLANs'
        template_name = 'inc/table.html'
        fields = (
            'vid',
            'vlans'
        )
