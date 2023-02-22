from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


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
