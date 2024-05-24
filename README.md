# NetBox VLAN Manager

NetBox plugin for viewer of multiple VLAN Group spaces.

![PyPI](https://img.shields.io/pypi/v/netbox-vlan-manager)
![publish PyPI workflow](https://github.com/miyuk/netbox-vlan-manager/actions/workflows/pub-pypi.yml/badge.svg)

## Purpose

Enterprise environment has a lot of routers or switches.
These devices manage VLAN each other.

In many cases, these manage as one VLAN group.
On the other hand, complex network has multiple VLAN groups

For example, below cases.

- Manage multi site VLAN groups
- Visualize Cisco ACI Leaf Switch VLANs

NetBox can manage VLAN space as `VLAN Group`.
However, it can one VLAN Group only.

NetBox VLAN Manager manage multiple `VLAN Group` as `VLAN Group Set`, and visualize status in tabular form such as below image.

![VLAN Group Set VLANs](https://raw.githubusercontent.com/miyuk/netbox-vlan-manager/main/docs/img/vlan_group_overview.png)

## Features

### Models

This plugin provides following Models:

- VLAN Group Set
  - Manage multiple VLAN Group

### API

This plugin provides following API:

- Available VLAN
  - Extract none used VID searching all VLAN Groups

## Compatibility

This plugin requires NetBox `v3.4.0` or later because has migration scripts compatibility.

The compatibility table between plugin versions and netbox is as follows.

|NetBox version|Plugin version|
|---|---|
|3.x.x|0.1.x|
|4.x.x|0.2.x|

## Installation

The plugin is available as a Python package in PyPI and can be installed with pip:

```bash
pip install netbox-vlan-manager
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py

```python
PLUGINS = ['netbox_vlan_manager']
```

Restart NetBox

## Configuration

Currently, this plugin is not necessary plugin configuration

## Screenshots

VLAN Group Set List
![VLAN Group Set List](https://raw.githubusercontent.com/miyuk/netbox-vlan-manager/main/docs/img/vlan_group_set_list.png)

VLAN Group View Set with VLANs
![VLAN Group Set VLANs](https://raw.githubusercontent.com/miyuk/netbox-vlan-manager/main/docs/img/vlan_group_set_vlans.png)
