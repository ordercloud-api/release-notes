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

def get_versions():

	'''
		objective: parse a json file into versions
	'''

	#jsonLoc = 'Timeline-Massage.json'
	jsonLoc = 'Timeline.json'


	jsonFile = {}
	versions = []
	with open(jsonLoc, 'r') as f:

		jsonFile = json.load(f)
		#print(type(jsonFile))
		versions=(jsonFile)


	return (versions)



def fill_document(doc):
	"""Add a section, a subsection and some text to the document.

	:param doc: the document
	:type doc: :class:`pylatex.document.Document` instance
	"""


	versions = get_versions()

	#print(type(versions))
	#print(len(jsonFile))
	print(versions['1.0.80'])

	for item in versions.items():
		
		with doc.create(Section(item[1]['title'], numbering=False, label=False)):
			with doc.create(Paragraph(title= '', numbering=False, label=False)):
				doc.append(item[1]['summary'])

		for part in item[1]['changelog']:
			with doc.create(Paragraph(title= '', numbering=False, label=False)):
				doc.append(part)

		

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