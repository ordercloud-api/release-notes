from bs4 import BeautifulSoup
import markdown
from pathlib import Path
import json
from collections import OrderedDict
import re
from pylatex import Document, Section, Subsection, Command, LineBreak, NewLine
from pylatex.utils import italic, NoEscape
from pylatex.section import Paragraph
from operator import itemgetter
from datetime import datetime

def get_json():

	#jsonLoc = 'Timeline-Massage.json'
	jsonLoc = 'Timeline.json'


	jsonFile = {}
	versions = []
	with open(jsonLoc, 'r') as f:

		jsonFile = json.load(f)
		print(type(jsonFile))
		versions=(jsonFile)


	#versions = sorted(versions, key=itemgetter(1))

	return (versions)



def fill_document(doc):
	"""Add a section, a subsection and some text to the document.

	:param doc: the document
	:type doc: :class:`pylatex.document.Document` instance
	"""
	versions = get_json()

	print(type(versions))
	#print(len(jsonFile))
	print(versions.keys())

	for item in versions.items():
		print(item[1].keys())
		with doc.create(Section(item[1]['title'], numbering=False, label=False)):
			with doc.create(Paragraph(title= '', numbering=False, label=False)):
				doc.append(item[1]['summary'])
			with doc.create(Paragraph(title= '', numbering=False, label=False)):
				doc.append(item[1]['changelog'])


'''
	for i in versions: # sorted by time rn
		#print(i)
		for item in jsonFile:
			#print(item['Meta']['Version Number'])
		#if item['Meta']['Version Number'] == 'v1.0.'+str(i[0]):
				with doc.create(Section('Release '+item['Meta']['Version Number'], numbering=False, label=False)):
					with doc.create(Paragraph(title= '', numbering=False, label=False)):
						doc.append('Released to Production: ' + item['Meta']['Released to Production'])
					with doc.create(Paragraph(title= '', numbering=False, label=False)):
						doc.append(item['Meta']['Summary'])

'''					

if __name__ == '__main__':

	# Document with `\maketitle` command activated
	doc = Document(documentclass='memoir', indent=4)

	doc.preamble.append(Command('title', 'OrderCloud Platform Timeline'))
	doc.preamble.append(Command('author', 'K.L.Reeher'))
	doc.preamble.append(Command('date', NoEscape(r'\today')))
	doc.append(NoEscape(r'\maketitle'))

	fill_document(doc)

	doc.generate_tex('ordercloud_timeline')
	#doc.generate_pdf('ordercloud_timeline', clean_tex=False)

	tex = doc.dumps()  # The document as string in LaTeX syntax