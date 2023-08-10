#!bin/python
# -*- coding: utf-8 -*-
#==========[Copyright: DrowKid]=================[Open Source]=============*
import os, sys
#======================[Keys/Args]=========================[✓]
path = "./.banners"
access_rights = 0o755
bpath = " ~/../../usr/bin"
hpath = " ~/../home/.drowkid/.cm"
fledit = '''#!bin/python
# -*- coding: utf-8 -*-
#=======================================[ Copyright: DrowKid ]=========================================>
#
#
#
#=======================================[ Open Source ]=========================================>

import os, sys

#=======================================[Alias]=========================================>


'''
fledit2 = ''' = input(" '''
p3 = "python3 "
banner = p3 + "./.banners/.banner-kid;"
bannerinit = p3 + "./.banners/.banner-init;"
#======================[Carpetas]=========================[✓]
try:
    os.mkdir(path, access_rights)
except OSError:
    print("")
else:
    print("")

#======================[Banner]=========================[✓]
os.system(banner + bannerinit)

#======================[Creación del alias]=========================[✓]
nombre = input('¿Nombre del alias?: Ej. (cl),(n) R: ')
cm = "chmod 777 " + nombre + ";"
file = input('''¿Contenido del comando?
Ej: "clear", "wget". R: ''')
pregunta = input('''¿Qué pregunta será realizada para ejecutar el comando?
Ej: "¿Cuál es la url del repositorio?(para git clone). R: ''')
fledit3 = pregunta
fl = '''")'''
comando = file
com = comando + ''' " + ''' + nombre + ''' )'''
fledit1 = nombre + fledit2 + fledit3 + '''")''' + '''
os.system("''' + com
#======================[Asignación del alias ]=========================[✓]
try:
    f = open(nombre, "a", encoding="utf8")
    f.write(fledit +fledit1)
    f.close()
except OSError:
    print("")
else:
    print("")
os.system("mv " + nombre + hpath)
os.system('echo "cd;cd .drowkid/.cm;python3 ' + nombre + '">>' + nombre)
mv = "mv " + nombre + " ~/../usr/bin;"
os.system(cm + mv)
#=======================================[ Fin ]=========================================>
os.system('echo "cd;cd .drowkid/.cm;python3 init.py">>alias;chmod 775 alias;mv alias ~/../usr/bin')
