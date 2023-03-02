# NetBox VLAN Manager

NetBox plugin for viewer of multiple VLAN Group spaces.

![PyPI](https://img.shields.io/pypi/v/netbox-vlan-manager)
![publish PyPI workflow](https://github.com/miyuk/netbox-vlan-manager/actions/workflows/pub-pypi.yml/badge.svg)

## Features

This plugin provide following Models:

- VLAN Group Set

## Compatibility

Each Plugin Version listed below has been tested with its corresponding NetBox Version.

| NetBox Version | Plugin Version |
| :------------: | :------------: |
|      3.4       |     0.0.1      |

## Installation

The plugin is available as a Python package in PyPI and can be installed with pip:

```bash
pip install netbox-vlan-manager
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py

```python
PLUGINS = ['netbox-vlan-manager']
```

Restart NetBox

## Configuration

Currently, This plugin is not necessary plugin configuration

## Screenshots

VLAN Group Set List
![VLAN Group Set List](https://raw.githubusercontent.com/miyuk/netbox-vlan-manager/main/docs/img/vlan_group_set_list.png)

VLAN Group View Set with VLANs
![VLAN Group Set VLANs](https://raw.githubusercontent.com/miyuk/netbox-vlan-manager/main/docs/img/vlan_group_set_vlans.png)
