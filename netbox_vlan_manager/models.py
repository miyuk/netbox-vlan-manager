from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from ipam.models import VLAN


class VLANGroupSet(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    vlan_groups = models.ManyToManyField(
        to='ipam.VLANGroup',
        related_name='vlan_group_sets',
        blank=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'plugins:netbox_vlan_manager:vlangroupset', kwargs={'pk': self.pk})

    @property
    def min_vid(self):
        return min(self.vlan_groups.all(), key=(lambda x: x.min_vid)).min_vid

    @property
    def max_vid(self):
        return max(self.vlan_groups.all(), key=(lambda x: x.max_vid)).max_vid

    @property
    def vlans(self):
        vlan_groups = self.vlan_groups.all()
        group_vlans = VLAN.objects.filter(
            group__in=vlan_groups).select_related('group')

        vlan_group_vlans = []
        for vid in range(self.min_vid, self.max_vid + 1):
            item = {}
            item['vid'] = vid
            vlans = [x for x in group_vlans if x.vid == vid]
            item['vlans'] = vlans
            item['status'] = 'Available' if not vlans else 'Assigned'
            vlan_group_vlans.append(item)
        return vlan_group_vlans

    def get_available_vids(self):
        available_vlans = set([x['vid']
                               for x in self.vlans if x['status'] == 'Available'])

        return sorted(available_vlans)

    def get_next_available_vid(self):
        available_vids = self.get_available_vids()
        if available_vids:
            return available_vids[0]
        return None
