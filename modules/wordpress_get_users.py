import urllib2, urllib
import re
from colorama import *

ARGS = {
    'URL' : '',
    'MAXUSERS' : '5'
}

def getUsers(site, nbusers) :
    userlist = []
    i = 1
    while( i <= nbusers ) :
        url = site + '?author=%i' % i
        try:
            html = urllib2.urlopen(url).read()
        except  :
            print Fore.RED +'[-] The page returned ->', str(urllib.urlopen(url).getcode()) + Fore.RESET        
        re1 = re.findall("<title>(.*?)</title>" , html)
        user = re.search("(.*?) |" , re1[0]).group(1)
        userlist.append(user)          
        i += 1
           
    return userlist

def bambam() :
    a = getUsers(ARGS['URL'], int(ARGS['MAXUSERS']))
    if a :
        print Fore.GREEN + '[+] Found '+ str(len(a)) + ' users : ' + Fore.RESET
        print '\n'.join(a)