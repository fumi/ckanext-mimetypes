from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-mimetypes',
    version=version,
    description="Custom MIME types extension",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Fumihiro Kato',
    author_email='fumi@fumi.me',
    url='http://fumi.me',
    license='Affero GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.mimetypes'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.mimetypes.plugin:PluginClass
    ''',
)
