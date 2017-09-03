from __future__ import print_function

import sys
import os.path as op
import time

rpws_folder = op.dirname(op.dirname(__file__))
sys.path.append(rpws_folder)
print('sys.path + {}'.format(rpws_folder))

import rpws

import testconfig as config


rs = rpws.RevitServer(config.test_server_name, config.test_server_version)


print("\nTesting server info -------------------------------------------------")
print(rs, end='\n')
print(rs.path, end='\n')
print(rs._api_path(), end='\n')


sinfo = rs.getinfo()
print(sinfo.name, end='\n')
print(sinfo.version, end='\n')
print(sinfo.machine_name, end='\n')
print(sinfo.roles, end='\n')
print(sinfo.access_level_types, end='\n')
print(sinfo.max_path_length, end='\n')
print(sinfo.max_name_length, end='\n')
print(sinfo.servers, end='\n')

sdriveinfo = rs.getdriveinfo()
print(sdriveinfo.drive_space, end='\n')
print(sdriveinfo.drive_freespace, end='\n')


print("\nTesting server listfiles and getfileinfo --------------------------")
for m in rs.listfiles():
    print(m)


print("\nTesting server listfolders and getfolderinfo ------------------------")
for f in rs.listfolders():
    print(f.name)
    print(f.path)
    print(f.locks_inprogress)
    print(rs.getfolderinfo(f.path))


print("\nTesting server listmodels and getmodelinfo --------------------------")
for m in rs.listmodels(config.test_folder):
    print(m.name)
    print(m.path)
    print(m.locks_inprogress)
    print(rs.getmodelinfo(m.path))


print("\nTesting server getprojectinfo ---------------------------------------")
for m in rs.listmodels(config.test_folder):
    print(m.name)
    print(m.path)
    print(rs.getmodelinfo(m.path))
    for p in rs.getprojectinfo(m.path).parameters:
        print(p)

print("\nTesting server lock -------------------------------------------------")
rs.lock(config.test_file)
try:
    rs.lock(config.test_folder)
except rpws.ServerForbiddenError:
    print('Success')

print("\nTesting server unlock -----------------------------------------------")
rs.unlock(config.test_file)
rs.unlock(config.test_folder)

print("\nTesting server mkdir- -----------------------------------------------")
rs.mkdir(config.test_mkfolder)

print("\nTesting server rename -----------------------------------------------")
rs.rename(config.test_mkfolder, config.test_newfoldername)

print("\nTesting server delete- -----------------------------------------------")
rs.rmdir(config.test_renamedfolder)

print("\nTesting server copy -------------------------------------------------")
rs.copy(config.test_file, config.test_cpyfile, overwrite=True)

print("\nTesting server move -------------------------------------------------")
rs.move(config.test_cpyfile, config.test_mvfile, overwrite=True)

time.sleep(1)
rs.delete(config.test_mvfile)


print("\nTesting model history------------------------------------------------")
for h in rs.getmodelhistory(config.test_mhistory).items:
    print(h)


print("\nTesting descendent locks --------------------------------------------")
for h in rs.getdescendentlocks(config.test_folder).items:
    print(h)

for h in rs.deletedescendentlocks(config.test_folder):
    print(h)
