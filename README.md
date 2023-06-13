# NetBox VLAN Manager

NetBox plugin for viewer of multiple VLAN Group spaces.

![PyPI](https://img.shields.io/pypi/v/netbox-vlan-manager)
![publish PyPI workflow](https://github.com/miyuk/netbox-vlan-manager/actions/workflows/pub-pypi.yml/badge.svg)


## Purpose

Enterprise environment has a lot of routers or switches.
These devices manage VLAN each other.

In many case, these manage one VLAN space.
On the other hand, complex network has multiple VLAN spaces

For example, below cases.

- Manage Head Quarter and Branch building WAN and LAN VLANs
- Visualize Cisco ACI Leaf Switch VLANs using Global Scope [*](https://learningnetwork.cisco.com/s/article/l2-interface-policy-global-scope-port-local-scope)

NetBox can manage VLAN space as `VLAN Group`.
However, it can one VLAN Group only.

NetBox VLAN Manager manage multiple `VLAN Group` as `VLAN Group Set`, and visualize status in tabular form


## Features

### Models

This plugin provide following Models:

- VLAN Group Set
    - Manage multiple VLAN Group

### API

This plugin provide following API:

- Avaiable VLAN
    - Extract none used VID searching all VLAN Groups

## Compatibility

Each Plugin Version listed below has been tested with its corresponding NetBox Version.

| NetBox Version | Plugin Version |
| :------------: | :------------: |
|      3.4       |     0.0.1      |
|      3.5       |     0.0.4      |

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
