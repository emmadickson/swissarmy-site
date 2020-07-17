#!/usr/bin/python

import sys
import os 
import datetime
import re 
from bs4 import BeautifulSoup
import json

passed_site = (sys.argv[1])

dict = {}
domain_name = passed_site.split("/")

filename = '%s_info.json' % domain_name[len(domain_name)-1][:-5]

parsed_file = open(passed_site).read()
parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
soup = BeautifulSoup(parsed_file, parser)

dict['a_tag'] = []
dict['link_tag'] = []
dict['img'] = []
dict['scripts'] = []

for link in soup.find_all('a', href=True):
    found_link = (link['href'])
    dict['a_tag'].append(found_link)
    
for link in soup.find_all('img'):
    img = (link['src'])  
    dict['img'].append(img)

for link in soup.find_all('script'):
    script = (link['src'])    
    dict['scripts'].append(script)
    
for link in soup.find_all('link'):
    link = (link['href'])   
    dict['link_tag'].append(found_link) 
    
r = json.dumps(dict)
with open(filename, "w") as f:
    f.write(r)