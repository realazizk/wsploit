import urllib2
import re
from colorama import *

def pathDiscloure(self) :
    error = urllib2.urlopen(self.site).read()
    if error is not None :
        return None
    else :
        return ("[" + self.body.replace("<b>", '').replace("</b>", "").replace("<br />", "").strip("\n")+"]").strip()

