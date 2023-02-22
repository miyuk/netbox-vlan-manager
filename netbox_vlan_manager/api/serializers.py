from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import VLANGroupSet


class VLANGroupSetSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=f'plugins-api:netbox_vlan_manager-api:vlangroupset-detail'
    )
    vlan_group_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = VLANGroupSet
        fields = (
            'id',
            'url',
            'display',
            'name',
            'description',
            'comments',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
            'vlan_group_count',
        )
