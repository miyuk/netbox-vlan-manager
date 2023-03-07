from django import template
register = template.Library()


@register.filter
def get_vlan_by_group(record, vlan_group):
    vlan = record['vlans'].filter(group=vlan_group).first()
    return vlan
