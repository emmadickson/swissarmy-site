#!/usr/bin/python

import sys
import os
import json

PATH = (sys.argv[1])
filename = 'general_info.json'
dict = {}
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(PATH):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

for file in listOfFiles:
    ending = file.split('.')
    if len(ending) == 2:
        if 'git' in ending[1]:
            if 'git' in dict.keys():
                dict['git'].append(".".join(ending))
            else:
                dict['git'] = [".".join(ending)]
        elif ending[1] in dict.keys():
            dict[ending[1]].append(".".join(ending))
        else:
            dict[ending[1]] = [".".join(ending)]
    
            
r = json.dumps(dict)
with open(filename, "w") as f:
    f.write(r)