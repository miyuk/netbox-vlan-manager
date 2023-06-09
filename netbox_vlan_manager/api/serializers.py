from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
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


class NestedVLANGroupSetSerializer(WritableNestedSerializer):
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
            'vlan_group_count',
        )


class AvailableVLANSerializer(serializers.Serializer):
    vid = serializers.IntegerField(read_only=True)
    group_set = NestedVLANGroupSetSerializer(read_only=True)

    def to_representation(self, instance):
        return {
            'vid': instance,
            'group_set': NestedVLANGroupSetSerializer(
                self.context['group_set'],
                context={'request': self.context['request']}
            ).data,
        }
