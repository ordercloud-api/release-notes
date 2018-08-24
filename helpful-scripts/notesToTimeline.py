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
import feedparser



class ApiVersion(object):
	"""
	an api release version which is comparable

	version: float, version #
	title: version title
	link: release notes link
	summary: exec summary
	contents: changelog
	"""

	def __init__(self, version, title='', link='', summary='', contents=''):
		self.version = version
		self.title = title
		self.link = link
		self.summary = summary 
		self.contents = contents

	def __getitem__(self, key):

		return self.key

	def __setitem__(self, key, value):
		self.key = value

		return self.key

	def __repr__(self):

		return '\nApiVersion: \n title: '+self.title+' \n version: '+self.version+'\n link: '+self.link+'\n summary: '+self.summary+'\n contents: '+repr(self.contents)

def formatContents(versions):

	for item in versions:
		#print(type(item))
		#print(item)

		listText = []

		soup = BeautifulSoup((item.contents), 'html.parser')
		#print(item.contents)
		fullText = soup.p.text
		
		for s in list(soup.find_all('p')[1:]):

			listText.append(s.text)

		#print(listText)

		item.contents=listText

	print(versions)

	return versions

def getVersionsFromXML(xmlPath):

	d = feedparser.parse(xmlPath)

	print(d.encoding)

	versions = []

	for release in d.entries:
		content = []
		verNum = ''
		if re.search(r'[^v][\d\.][\S]+', release.title) is not None:
			verNum = re.search(r'[^v][\d\.][\S]+', release.title).group(0)
		else:
			continue
		for item in release.content:
			content.append(item['value'])

		version = ApiVersion(verNum, release.title, release.link, '', ''.join(content))
		versions.append(version)


	return versions



def main():

	versions = getVersionsFromXML('https://ordercloud-api.github.io/release-notes/feeds/api-release-notes.atom.xml')
	
	finetuned = formatContents(versions)

	with open('Timeline.json', 'w') as f:


		timeline = {}
		
		
		for item in finetuned:
			version = {
				'title' : item.title,
				'version' : item.version,
				'summary' : item.summary,
				'changelog' : item.contents,
				'release notes link' : item.link

			}
			timeline[item.version] = version
			
		json.dump(timeline, f, indent=4, sort_keys=False)

		



main()