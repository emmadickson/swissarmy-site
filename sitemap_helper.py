#!/usr/bin/python
import sys
import os 
import datetime
from bs4 import BeautifulSoup

passed_site = (sys.argv[1])

domain_name = passed_site.split("/")

filename = '%s_sitemap.xml' % domain_name[len(domain_name)-1][:-5]
print(filename)
domain_name = domain_name[0:len(domain_name)-1]
domain_name = "/".join(domain_name) + "/"


parsed_file = open(passed_site).read()

parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
soup = BeautifulSoup(parsed_file, parser)
with open(filename, "w") as f:
    t = os.path.getmtime(passed_site)
    time = (datetime.datetime.fromtimestamp(t))
    body = '''<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>%s</loc>
            <lastmod>%s</lastmod>
        </url>\n''' % (passed_site, time)
    f.write(body)
    for link in soup.find_all('a', href=True):
        found_link = (link['href'])
        if found_link != 'index.html' and len(found_link) > 2:
            found_link = domain_name + found_link
            t = os.path.getmtime(found_link)
            time = (datetime.datetime.fromtimestamp(t))
            body = '''        <url>
             <loc>%s</loc>
             <lastmod>%s</lastmod>
        </url>\n'''  % (found_link, time)
            f.write(body)
    f.write("</urlset>")
