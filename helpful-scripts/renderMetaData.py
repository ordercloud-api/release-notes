import pathlib, os, glob, fnmatch, re, datetime, operator, calendar
import logging, sys
from pathlib import Path

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# render pelican site metadata from files

versions = glob.glob('content/v*.md', recursive = True)

filenames = []

for filename in versions:
	filename = filename.replace('.md','')
	filename = filename.split('\\v')
	filenames.append(filename[1])

#print(versions)
#print(filenames)
logging.debug('starting file processing...')
for index in range(len(filenames)):
	with open('content/v'+filenames[index]+'.md', 'r', encoding="utf8") as original: 
		data = original.read()
		#logging.debug(data)

		data = re.split('\(.+\/.+\n+#.+\n', data)

		with open('content/v'+filenames[index]+'.md', 'w', encoding="utf8") as output:
			output.write('---\nTitle: API v1.0.'+filenames[index]+' Release Notes\nCategory: release-notes\n Tags: \nSlug: 1.0.'+filenames[index]+'-release-notes\nAuthors: Kate Reeher\n---\n')
		with open('content/v'+filenames[index]+'.md', 'a', encoding="utf8") as output:
			output.write(data[1])

