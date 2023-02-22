from extras.plugins import PluginMenuItem, PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

vlan_group_manager_buttons = [
    PluginMenuButton(
        link=f'plugins:netbox_vlan_manager:vlangroupset_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link=f'plugins:netbox_vlan_manager:vlangroupset_list',
        link_text='VLAN Group Set',
        buttons=vlan_group_manager_buttons
    ),
)
