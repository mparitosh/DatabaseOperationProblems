import urllib2
import re

#req = urllib2.Request('http://www.tennisabstract.com/cgi-bin/player.cgi?p=RogerFederer')
response = urllib2.Request('http://www.tennisabstract.com/cgi-bin/player.cgi?p=RogerFederer')
the_page = urllib2.urlopen(response).read()
#print(the_page)
paragraphs = re.findall(r'ptable',str(the_page))
for eachP in paragraphs:
    print(eachP)
