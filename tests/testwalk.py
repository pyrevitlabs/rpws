import sys
import os.path as op

rpws_folder = op.dirname(op.dirname(__file__))
sys.path.append(rpws_folder)
print('sys.path + {}'.format(rpws_folder))

from rpws import RevitServer

import testconfig as config


rs = RevitServer(config.test_server_name, config.test_server_version)


for parent, folders, files, models in rs.walk(config.test_folder):
    print(parent)
    for fd in folders:
        print('\t@d {}'.format(fd.path))
    for f in files:
        print('\t@f {}'.format(f.path))
    for m in models:
        print('\t@m {}'.format(m.path))
