import pathlib, os, glob, fnmatch, re, datetime
from pathlib import Path



p = Path('.')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']

#list (p.glob('**/*'.md))

# could be worth parsing the blob of .md files into an ordered object; could then iterate over the object to produce month level readmes too.

with open('README.md', 'w') as output:
			output.write('# OrderCloud Release Notes \n*Release notes for the OrderCloud API*\n')
			sorter = sorted(glob.glob('**/*.md', recursive = True))
			for filename in sorter:
				if fnmatch.fnmatch(filename, '20??/README.md'):
					file = re.search(r'\d+', filename)
					output.write('\n## ' + '[' + file.group(0) + '](' + str(filename)+ ')\n')
				if fnmatch.fnmatch(filename, '20??/*/README.md'):
					file = re.search(r'\w[a-z]+', filename)
					output.write('\n### ' + '[' + str(file.group(0)) + '](' + str(filename)+ ')\n')
				if fnmatch.fnmatch(filename, '20??/*/v*.md'):
					file = re.search(r'v\d+', filename)
					output.write('- ' + '[' + str(file.group(0)) + '](' + str(filename)+ ')\n')
