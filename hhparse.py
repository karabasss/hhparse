#!/usr/bin/env python
'''
packages is needed:

yum install python-pip     
pip install BeautifulSoup 
'''
import lxml.html as html
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import re, os, sys
from optparse import OptionParser

#####VARS#####
dirname = 'htmls'
filename = 'hhlinks.txt'
##############
def parseArgs():
    
    parser = OptionParser()
    parser.add_option("-u",
                      action="store",
                      dest="mylink",
                      default=False,
                      help="takes link to hh.ru as argument")
    (options, args) = parser.parse_args()
    if len(sys.argv[1:]) > 0:
        mylink = options.mylink
        return mylink
    else:
        print "You can pass url in quotes with '-u' flag like [root@o182]# python hhparse.py -u \"http://spb.hh.ru/blabla\"" 
        mylink = raw_input("Paste link please: ")
        return mylink
    
def createDir(x):
    if not os.path.exists('htmls'):
        try:
            os.makedirs('htmls')
        except Exception:
            print "Error creating subdirectory!"

def parseandStore():

    name = 1  # first name for html (1.html, 2.html ... etc)
    
    for i in soup.findAll('a', attrs={'href': re.compile("^/resume/")}):
        worklink = "https://spb.hh.ru/" + i.get('href')
        hhlinks.write(worklink + '\n')
        #### store html links from urls
        response = urllib2.urlopen(worklink)
        webContent = response.read()
        try:
            htmlfile = open(os.path.join('htmls', '%s.html' % name), 'w')
        except Exception:
            print "Error creating files in directory 'htmls'!"
        name +=1
        htmlfile.write(webContent)
        htmlfile.close

mylink = parseArgs()
#mylink = raw_input("Paste link please: ")
# or:
# mylink = "your hh link" ###
print "Yor link is: "
print "==================================================="
print mylink
print "==================================================="
hhlinks = open(filename, 'w')
url = urllib.urlopen(mylink)
soup = BeautifulSoup(url)
####
createDir(dirname)
parseandStore()
hhlinks.close()
#### 
