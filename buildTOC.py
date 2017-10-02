import pathlib
from pathlib import Path
import os
import glob
import fnmatch
import re


p = Path('.')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']

#list (p.glob('**/*'.md))

with open('README.md', 'w') as output:
			output.write('# OrderCloud Release Notes \n*Release notes for the OrderCloud API*\n')
			for filename in glob.glob('**/*.md', recursive = True):
				if fnmatch.fnmatch(filename, '20??/README.md'):
					file = re.search(r'\d+', filename)
					output.write('\n## ' + '[' + file.group(0) + '](' + str(filename)+ ')\n')
				if fnmatch.fnmatch(filename, '20??/*/README.md'):
					file = re.search(r'\w[a-z]+', filename)
					output.write('\n### ' + '[' + str(file.group(0)) + '](' + str(filename)+ ')\n')
				if fnmatch.fnmatch(filename, '20??/*/v*.md'):
					file = re.search(r'v\d+', filename)
					output.write('- ' + '[' + str(file.group(0)) + '](' + str(filename)+ ')\n')
