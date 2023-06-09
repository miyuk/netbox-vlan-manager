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
    def vlans(self):
        vlan_groups = self.vlan_groups.all()
        max_vid = max(vlan_groups, key=(lambda x: x.max_vid)).max_vid
        min_vid = min(vlan_groups, key=(lambda x: x.min_vid)).min_vid

        vlan_group_vlans = []
        for vid in range(min_vid, max_vid + 1):
            item = {}
            item['vid'] = vid
            vlans = VLAN.objects.filter(vid=vid, group__in=vlan_groups)
            item['vlans'] = vlans
            item['status'] = 'Available' if not vlans else 'In Use'
            vlan_group_vlans.append(item)
        return vlan_group_vlans

    def get_available_vids(self):
        vlan_groups = self.vlan_groups.all()
        max_vid = max(vlan_groups, key=(lambda x: x.max_vid)).max_vid
        min_vid = min(vlan_groups, key=(lambda x: x.min_vid)).min_vid

        available_vlans = {
            vid for vid in range(min_vid, max_vid + 1)
        }
        for vlan_group in vlan_groups:
            available_vlans -= set(
                VLAN.objects.filter(group=vlan_group).values_list(
                    'vid', flat=True
                )
            )

        return sorted(available_vlans)

    def get_next_available_vid(self):
        available_vids = self.get_available_vids()
        if available_vids:
            return available_vids[0]
        return None
