#! notesToTimeline.py

# open file

'''
API Version, Release Date, Features, Bug Fixes
1.0.X , date, stuff

'''

from bs4 import BeautifulSoup
import markdown
from pathlib import Path
import json
import re

def getVersions():

	p = Path('../content/API-ReleaseNotes')

	versions = []

	for child in p.iterdir():
		versions.append(child)

	#print(versions)

	return versions



def getFeatures(version):

	path = Path(version)

	#print(path)

	try:
		f = open(path, 'r', encoding='utf-8')
		fileString = f.read()
		html=markdown.markdown( fileString )
	except: # catch *all* exceptions
	  e = sys.exc_info()[0]
	  write_to_page( "<p>Error: %s</p>" % e )


	soup = BeautifulSoup(html, "html.parser")

	#print(soup.prettify())
	
	date = soup.find('p')
	#print(date.contents)
	date = ''+str(date.contents[0].string)
	#print(date)
	#print(type(date))

	date = re.search('Date:.\w.+[^"]', date)

	date = (date.group(0)[6:])
	print(date)
	meta = {}

	meta["Summary"]= ""
	meta["Released to Production"] = '2018-01-03 00:00 CDT'
	meta["Breaking Changes"] = False

	if len(version.stem) > 5:
		meta['Version Number'] = version.stem
	elif len(version.stem) <= 5:
		meta['Version Number'] = 'v1.0.'+version.stem[1:]
	
	meta['Date'] = date



	bits = {}
	

	for header in soup.find_all('h2'):
		#print('HEADER: '+header.string)
		headerStr = str(header.string)
		bits[headerStr] = []
		for sibling in header.find_all_next():
			#print(sibling)
			if 'h2' not in sibling:
				bits[headerStr].append(str(sibling))
			else: 
				break

	

	total = {}


	total["Meta"] = meta
	total["Features"] = bits

	return total

#print(features.strings)


def main():

	versions = []
	versions = getVersions()

	print(versions)

	features = []

	for version in versions:
		features.append(getFeatures(version))

	with open('Timeline.json', 'a') as f:
		timeline = {}
		timeline['Data'] = []
		
		for item in features:
			timeline['Data'].append(item)
			
		json.dump(timeline, f, indent=4, sort_keys=False)








main()