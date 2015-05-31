from os import listdir
from os.path import isfile, join

def getExtension(myfile) :
  return join('modules',myfile).split('.')[1]

def showmodules() :
  onlyfiles = [ f[:-3] for f in listdir('modules') if isfile(join('modules',f)) and  getExtension(f) == 'py']
  onlyfiles.remove('__init__')
  return onlyfiles

#~ def getdiscription(myfile) :
    #~ 
