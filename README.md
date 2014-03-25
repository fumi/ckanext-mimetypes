ckanext-mimetypes
=================

Custom mimetypes extension

Read the Custom Internet media types (MIME types) section 
at http://ckan.readthedocs.org/en/latest/maintaining/filestore.html

Install
-------
Clone this repository and ```run python setup.py install``` to install simply. Or you can install the following way.

```
$ pip install -e git+https://github.com/fumi/ckanext-mimetypes.git#egg=ckanext-mimetypes
$ cd [this repo]
$ python setup.py develop
```
    
Then add ```mimetypes``` to your ckan.plugins in your CKAN config file.
