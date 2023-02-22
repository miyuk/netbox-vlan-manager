from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from ipam.models import VLANGroup
from .models import VLANGroupSet


class VLANGroupSetForm(NetBoxModelForm):
    vlan_groups = DynamicModelMultipleChoiceField(
        queryset=VLANGroup.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = VLANGroupSet
        fields = (
            'name',
            'vlan_groups',
            'description',
            'comments',
            'tags'
        )
