import codecs
import os.path

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


long_description = read("README.md")

setup(
    name='netbox-vlan-manager',
    version=get_version('netbox_vlan_manager/version.py'),
    description='VLAN Manager for multiple VLAN Groups',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miyuk/netbox-vlan-manager/",
    author='miyuk',
    author_email='miyuk@miyuk.net',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ]
)
