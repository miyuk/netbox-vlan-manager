from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path(
        'vlan-group-sets/',
        views.VLANGroupSetListView.as_view(),
        name='vlangroupset_list'
    ),
    path(
        'vlan-group-sets/add/',
        views.VLANGroupSetEditView.as_view(),
        name='vlangroupset_add'
    ),
    path(
        'vlan-group-sets/<int:pk>/',
        views.VLANGroupSetView.as_view(),
        name='vlangroupset'
    ),
    path(
        'vlan-group-sets/<int:pk>/edit/',
        views.VLANGroupSetEditView.as_view(),
        name='vlangroupset_edit'
    ),
    path(
        'vlan-group-sets/<int:pk>/delete/',
        views.VLANGroupSetDeleteView.as_view(),
        name='vlangroupset_delete'
    ),
    path(
        'vlan-group-sets/<int:pk>/changelog/',
        ObjectChangeLogView.as_view(),
        name='vlangroupset_changelog',
        kwargs={
            'model': models.VLANGroupSet
        }
    ),
    path(
        'vlan-group-sets/<int:pk>/export-vlans/',
        views.VLANGroupSetExportVLANs.as_view(),
        name='export_vlans'
    ),
)
