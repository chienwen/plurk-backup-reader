#!/usr/bin/python

import sys
import os
import re
import json
import csv

dirPath = sys.argv[1]
dataKeys = None

for fileName in os.listdir(dirPath):
    if not re.match(r'.*\.js$', fileName):
        continue
    with open(dirPath + '/' + fileName, 'r') as file:
        data = file.read().replace('\n', '')
        m = re.search(r'BackupData\.plurks\["(.+)"\]=(.+);', data)
        x = json.loads(m.group(2))
        if dataKeys is None:
            i = 0
            dataKeys = {}
            for k in x[0]:
                dataKeys[k] = i
                i += 1
        with open(dirPath + '/' + fileName + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            for line in x:
                dataLine = [None] * len(dataKeys)
                for k in line:
                    dataLine[dataKeys[k]] = line[k]
                writer.writerow(dataLine);

