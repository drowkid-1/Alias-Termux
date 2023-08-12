#!bin/python
# -*- coding: utf-8 -*-
#==========[Copyright: DrowKid]=================[Open Source]=============*
import os, sys
#======================[Keys/Args]=========================[✓]
banner = "cd;cd Alias-Termux/codes/.banners;python3 .banner-kid;"
bannerinit = "cd;cd Alias-Termux/codes/.banners;python3 .banner-init;"
#==================================[Banner]=======================================[✓]
os.system(banner)
os.system(bannerinit)

#==================================[Alias]=======================================[✓]
print ("El nombre del alias será utilizado para llamar al comando, es decir, si el nombre del alias es 'cl' y el comando a ejecutar o la tarea que debe realizar es 'clear', usando el nombre del alias (en este caso 'cl') desde cualquier ubicación de la terminal puedes llamarlo y ejecutarlo 'cl'")
nombre = input('¿Nombre del alias?: Ej. (cl),(n) R: ')
name = '.' + nombre 
chm = "chmod 777 " + nombre + ";"
comando = input('''¿Contenido del comando?
Ej: "clear", "wget". R: ''')
pregunta = input('''¿Qué pregunta será realizada para ejecutar el comando?
Ej: "¿Cuál es la url del repositorio?(para git clone). R: ''')
cierre = '''")'''

alias1 = '''#!bin/python
# -*- coding: utf-8 -*-
#=======================================[ Copyright: DrowKid ]=========================================>
#
#
#
#=======================================[ Open Source ]=========================================>

import os, sys

#=======================================[Alias]=========================================>


'''
alias2 = nombre + ''' = input("''' + pregunta + cierre + '''
os.system (' ''' + comando  + ''' ' + ''' + nombre + ''' )'''
bin = 'echo "cd;cd Alias-Termux/codes/.codes;python3 .' + nombre + '">>' + nombre + ';'
#======================[Asignación del alias ]=========================[✓]
try:
    f = open(name, "a", encoding="utf8")
    f.write(alias1 + alias2)
    f.close()
except OSError:
    print("")
else:
    print("") 
os.system('mv ' + name + ' ~/../home/Alias-Termux/codes/.codes')
os.system(bin +chm + 'mv ' + nombre + ' ~/../usr/bin')

