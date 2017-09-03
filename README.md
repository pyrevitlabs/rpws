## python wrapper for Autodesk Revit Server

This is a python module for interacting with Autodesk Revit Server using its RESTful API. This module depends on python `requests` for handling http requests to the Revit Server.

### Requires:
- for python 3
	- `requests` newer than 2.18.3
- for IronPython 2.7.7
	- `requests` exactly 2.13.0
	- `enum` newer than 1.1.6


### Installation:
- for python 3: `pip install rpws`
- for IronPython 2.7.7: Download this repository and copy the rpws folder to the IronPython `Lib/site-packages` folder.

### Module Files:

- `exceptions.py`: Defines module exceptions and custom exceptions for http status codes returned by the server
- `api.py`: Documents all standard keys that are returned in JSON dictionaries from server http API calls.
- `models.py`: Defines classes and namedtuples that wrap the data returned from server http API calls.
- `server.py`: Defines the server wrapper class. RevitServer class aims to support all the Revit Server http API functionality.

### Documentation:

[Read the documentation here](http://rpws.readthedocs.io/en/latest/#)

&nbsp;

## Examples:

#### Initializing a server

``` python
name = '<server name>'
version = '2017'    # server version in XXXX format
rserver = RevitServer(name, version)
```

#### Getting server info

``` python
# server root path
rserver.path

sinfo = rserver.getinfo()
sinfo.name
sinfo.version
sinfo.machine_name
sinfo.roles
sinfo.access_level_types
sinfo.max_path_length
sinfo.max_name_length
sinfo.servers

# server drive space and free space
sdriveinfo = rserver.getdriveinfo()
sdriveinfo.drive_space
sdriveinfo.drive_freespace
```


#### Listing All files, folders, and models

Make sure all paths start with root `/`

``` python
for parent, folders, files, models in rserver.walk():
     print(parent)
     for fd in folders:
         print('\t@d {}'.format(fd.path))
     for f in files:
         print('\t@f {}'.format(f.path))
     for m in models:
         print('\t@m {}'.format(m.path))
```

#### Locking, unlocking files, folders, and models

``` python
rserver.lock('/path/to/folder/or/model.rvt')
rserver.unlock('/path/to/folder/or/model.rvt')
```


#### Create, Move, Copy, Delete

``` python
rserver.mkdir('/path/to/folder')

rserver.rename('/path/to/folder/or/model.rvt',
               '/path/to/folder/or/model2.rvt')

rserver.rmdir('/path/to/folder/')
rserver.delete('/path/to/model.rvt')

rserver.copy('/path/to/folder/or/model.rvt',
             '/path/to/folder/or/model2.rvt', overwrite=True)

rserver.move('/path/to/folder/or/model.rvt',
             '/path/to/folder/or/model2.rvt', overwrite=True)
```

#### Getting model history

``` python
mhistory = rserver.getmodelhistory('/path/to/folder/or/model.rvt')
for hist_item in mhistory.items:
    print(hist_item.user, hist_item.date)
```
