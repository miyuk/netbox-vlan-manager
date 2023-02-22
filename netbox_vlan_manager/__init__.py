from extras.plugins import PluginConfig
from .version import __version__


class VLANManager(PluginConfig):
    name = 'netbox_vlan_manager'
    verbose_name = 'NetBox VLAN Manager'
    description = 'NetBox VLAN Manager for multitple VLAN Groups'
    author = 'miyuk'
    author_email = 'miyuk@miyuk.net'
    version = __version__
    base_url = 'vlan-manager'


config = VLANManager
