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
banner = p + ".banner-kid;"
bwelcome = p + ".bwelcome;"
os.system(banner + bwelcome)
#======================[Asignación del alias ]=========================[✓]
access_rights = 0o755
bpath = "./codes/.banners"
try:
    os.mkdir(bpath, access_rights)
except OSError:
    print("")
else:
    print("")
#======================[Asignación del alias ]=========================[✓]
path = "./.drowkid/.cm"
try:
    os.mkdir(path, access_rights)
except OSError:
    print("")
else:
    print("..")
#=======================================[init.py]=========================================>
os.system("cp init.py ~/../home/.drowkid/.cm")
os.system("mv .banner-init  .bannergit  .bannw .banner-kid   .banngc     .bwelcome ~/../home/KeysTermux/codes/.banners")
#=======================================[git clone]=========================================>
try:
    f = open(".gc", "a", encoding="utf8")
    f.write('''#!bin/python
import os, sys, time, requests
from time import sleep
os.system('cd;cd .drowkid/.cm;python3 .banngc')

sleep(1)

gc = "git clone "
url = input('Escriba la url del repositorio: ')
os.system(gc + url)''' )
    f.close()
except OSError:
    print("")
else:
    print("")
os.system("mv .gc ~/../home/.drowkid/.cm")
os.system('echo "cd;cd .drowkid/.cm;python3 .gc">>gc;chmod 775 gc;mv gc ~/../usr/bin')
#=======================================[WGET]=========================================[✓]

try:
    f = open(".w", "a", encoding="utf8")
    f.write('''#!bin/python
import os, sys, time, requests

from time import sleep

os.system('cd;cd .drowkid/.cm;python3 .bannw')
sleep(1)

w = "wget "
url = input('Escriba la URL del archivo/documento que desea descargar: ')
os.system(w + url)''' )
    f.close()
except OSError:
    print("")
else:
    print("")
os.system("mv .w ~/../home/.drowkid/.cm")
os.system('echo "cd;cd .drowkid/.cm;python3 .w">>w;chmod 775 w;mv w ~/../usr/bin')
#=======================================[aria2c]=========================================[✓]

