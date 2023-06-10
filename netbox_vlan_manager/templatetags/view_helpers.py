from django import template
register = template.Library()


@register.filter
def get_vlan_by_group(record, vlan_group):
    vlan = ([x for x in record['vlans'] if x.group == vlan_group] or [None])[0]
    return vlan
