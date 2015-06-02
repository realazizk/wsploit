import urllib2
import re
from colorama import *

ARGS = {
    'URL' : ''
}
COMMENT = 'Get wordpress version from readme.html'
AUTHOR = 'Mohamed Aziz (MatriX Coder)'

def getVersionRDme() :
    # get version from readme.html
    try :
        html = urllib2.urlopen(ARGS['URL'] + 'readme.html').read()
        return re.search('Version (.*)', html).group(1)
    except :
        return False
def bambam() :
    a = getVersionRDme()
    if a :
        print Fore.GREEN + '[*] Wordpress version is '+ a + Fore.RESET
    else :
        print Fore.RED + '[-] Could not find version or host is down' + Fore.REST