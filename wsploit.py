#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# The web hacker's toolkit
# Made to be simple :3


import sys
if sys.version_info > (3, 0) :
  print('[-] You need a python 2.7 installation')
  exit()

try :
  from colorama import *
except ImportError :
  print('[-] You need to install colorama module')

import subprocess
import readline
from core import show_modules

import importlib
try :
  from terminaltables import AsciiTable
except ImportError:
  print('[-] You need to install terminaltables module')
tab = [['Exploit Name', 'Comment']]
# init colorama
init()

# Logo :3
logo = """
██╗    ██╗███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██║    ██║██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║ █╗ ██║███████╗██████╔╝██║     ██║   ██║██║   ██║   
██║███╗██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
╚███╔███╔╝███████║██║     ███████╗╚██████╔╝██║   ██║   
 ╚══╝╚══╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
                                                       
"""

print(Fore.GREEN+logo+Fore.RESET)
print(Fore.MAGENTA+'\t----[ Loaded '+Fore.RESET+str(len(show_modules.showmodules()))+Fore.MAGENTA+' ]----'+Fore.RESET+'\n')

def execom(statement) :
  p = subprocess.Popen(statement[1:], shell=True, stderr=subprocess.PIPE)
  return p.stderr.read(1)

pr = Fore.CYAN+'wsploit >>> '+Fore.RESET
#moduli = ''
mod = None
while True :
  try :
    statement = raw_input(pr)
    if statement != '' :
      if statement[0] == '!' :
        execom(statement)
      elif statement == 'show modules' :
        modules = show_modules.showmodules()
        for modulei in modules:
          com = importlib.import_module('modules.'+modulei)
          # When comment attribute dont exist assign empty string
          try :
            module_comment = com.COMMENT
          except :
            module_comment = ''
          tab.append([modulei, module_comment])
        table = AsciiTable(tab)
        print('\n'+table.table+'\n')
      elif statement == 'exit' :
        print(Back.CYAN+'Good bye !'+Back.RESET)
        break
      elif statement[:4] == 'use ' :
        #moduli = statement[4:]
        try :
          mod = importlib.import_module('modules.'+statement[4:])
          pr = Fore.CYAN+'wsploit['+statement[4:]+']>>> '+Fore.RESET
        except :
          print(Fore.RED+'Module not found'+Fore.RESET)
      if mod != None :
        if statement == 'show options' :
          tab2 = [['Option', 'Value']]
          for key, value in mod.ARGS.iteritems() :
            tab2.append([key, value])
          table = AsciiTable(tab2)
          print('\n'+table.table+'\n')
        elif statement == 'unuse' :
          mod = None
          pr = Fore.CYAN+'wsploit >>> '+Fore.RESET
        elif statement[:4] == 'set ' :
          st = statement.split()
          mod.ARGS[st[1]] = st[2]
        elif statement[:6] == 'unset ' :
          st = statement.split()
          mod.ARGS[st[1]] = ''
        elif statement == 'exploit' :
          # Bambam lol don't ask me why :3
          mod.bambam()
  except KeyboardInterrupt:
    print('\n'+Back.CYAN+'Good bye !'+Back.RESET)
    break
  #except Exception as e:
  #  print Back.RED+str(e)+Back.RESET
  #  break
# Deinit colorama
deinit()
