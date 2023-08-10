#!bin/python
# -*- encoding: utf8 -*-
#|#|______________________________________________________________________
#|#|									|#|
#|#|		         COPYRIGHT: 	      DrowKid 		        |#|
#|#|									|#|
#|#|									|#|
#|#|									|#|
#|#|____________________________________________________________________|#|

import os, sys


#======================[Asignación del alias ]=========================[✓]
os.system("clear")
p = "python3 "
banner = p + "/codes/.banners/.banner-kid;"
bwelcome = p + "/codes/.banners/.bwelcome;"
os.system(banner + bwelcome)
#======================[Asignación del alias ]=========================[✓]
access_rights = 0o755
bpath = "/codes/.banners"
try:
    os.mkdir(bpath, access_rights)
except OSError:
    print("")
else:
    print("")
#======================[Asignación del alias ]=========================[✓]
path = "/../../.drowkid/.cm"
try:
    os.mkdir(path, access_rights)
except OSError:
    print("")
else:
    print("..")
#=======================================[init.py]=========================================>

#=======================================[git clone]=========================================>
try:
    f = open(".gc", "a", encoding="utf8")
    f.write('''#!bin/python
import os, sys, time, requests
from time import sleep

os.system('cd;cd KeysTermux/codes/.banners;python3 .banngc')
sleep(1)

gc = "git clone "
url = input('Escriba la url del repositorio: ')
os.system(gc + url)''' )
    f.close()
except OSError:
    print("")
else:
    print("")
os.system("mv .gc ~/../home/KeysTermux/codes")
os.system('echo "cd;cd KeysTermux/codes;python3 .gc">>gc;chmod 775 gc;mv gc ~/../usr/bin')
#=======================================[WGET]=========================================[✓]

try:
    f = open(".w", "a", encoding="utf8")
    f.write('''#!bin/python
import os, sys, time, requests

from time import sleep

os.system('cd;cd KeysTermux/codes/.banners;python3 .bannw')
sleep(1)

w = "wget "
url = input('Escriba la URL del archivo/documento que desea descargar: ')
os.system(w + url)''' )
    f.close()
except OSError:
    print("")
else:
    print("")
os.system("mv .w ~/../home/KeysTermux/codes")
os.system('echo "cd;cd KeysTermux/codes;python3 .w">>w;chmod 775 w;mv w ~/../usr/bin')
#=======================================[extras]=========================================[✓]
os.system('echo "cd;cd KeysTermux/codes;python3 alias.py">>alias.py;chmod 775 alias.py;mv alias.py ~/../usr/bin')
os.system('echo "cd;cd KeysTermux/codes;python3 init.py">>keys-t;chmod 775 keys-t;mv keys-t ~/../usr/bin')
