#!bin/python
# -*- coding: utf-8 -*-
#==========[Copyright: DrowKid]=================[Open Source]=============*
import os, sys
#======================[Keys/Args]=========================[✓]
access_rights = 0o755
bpath = " ~/../../usr/bin"
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
#======================[Banner]=========================[✓]
os.system(banner + bannerinit)

#======================[Creación del alias]=========================[✓]
print ("El nombre del alias será utilizado para llamar al comando, es decir, si el nombre del alias es 'cl' y el comando a ejecutar o la tarea que debe realizar es 'clear', usando el nombre del alias (en este caso 'cl') desde cualquier ubicación de la terminal puedes llamarlo y ejecutarlo 'cl')
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
os.system("mv " + nombre + " ~/../home/Alias-Termux/codes)
os.system('echo "cd;cd Alias-Termux/codes;python3 ' + nombre + '">>' + nombre)
mv = "mv " + nombre + " ~/../usr/bin;"
os.system(cm + mv)
