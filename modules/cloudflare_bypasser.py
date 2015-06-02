
import socket
from colorama import * 

ARGS = {
    'URL'     : '',
    'SUBDOM'  : 'mail;webmail;ftp;direct;cpanel',
    'VERBOSE' : '0'
}    
AUTHOR = 'Mohamed Aziz (MatriX Coder)'
COMMENT = 'A simple method to bypass cloudflare using subdomains'

def cloudflare(site) :
    subdoms = ARGS['SUBDOM'].split(';')
    site.replace('http://', '')
    site.replace('/', '')                  
    try:
        ip = socket.gethostbyname(site)
    except socket.error:
        Back.RED + '[-] Host is not reachable' + Back.RESET
        return
    for sub in subdoms:
        doo = sub + '.' + site
        if str(ARGS['VERBOSE']) != '0' :
            print ' [~] Trying -> ', doo
        try:
            ddd = socket.gethostbyname(doo)
            if ddd != ip:
                print Back.GREEN  + ' [*] Cloudflare bypassed -> '+ ddd+Back.RESET
                break
        except socket.error :
            Back.RED + '[-] Host is not reachable' + Back.RESET
            break

def bambam() :
    cloudflare(ARGS['URL'])