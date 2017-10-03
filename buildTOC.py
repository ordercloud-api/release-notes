import pathlib, os, glob, fnmatch, re, datetime, operator, calendar
from pathlib import Path

monthsIndex = {1:'January', 2:'February', 3:'March',4:'April',5:'May',6:'June', 7:'July', 8:'August',9:'September', 10:'October', 11:'November', 12:'December'}

versions = glob.glob('**/20??/*/v*.md', recursive = True)

sortedList = []
sortedMonths = []
sortedVersions = []
sortedYears = []

# [[2016, April, README]]

for filename in versions:
	filename = filename.split('\\')
	sortedList.append(filename)

# replace month name with month value for sorting
for k, v in monthsIndex.items():
	for item in sortedList:
		if item[1] == v:
			item[1]=k
			#print(item[1])


# sorts everything all nice (DOES NOT WORK IF REVERSE SORTED)
sortedList = sorted(sortedList, key=operator.itemgetter(0,1))

# add the year indexes to sortedYears
for index, item in enumerate(sortedList):
	print(item[0],index, item)
	if index == 0:
		sortedYears.append([item[0], 'README.md'])
	if item[0] > sortedList[index-1][0]:
		sortedYears.append([item[0], 'README.md'])

# add the month indexes to sortedMonths
for index, item in enumerate(sortedList):
	#print(index, item)
	if index == 0:
		sortedMonths.append([item[0], item[1], 'README.md'])
	elif item[1] == 'README.md':
		continue
	elif item[1] > sortedList[index-1][1]:
		sortedMonths.append([item[0], item[1], 'README.md'])

# write the markdown readme
with open('README.md', 'w') as output:
	output.write('\n# OrderCloud Release Notes \n*Release notes for the OrderCloud API*')	
	#output.write(str(sortedList))
	for indexY, year in enumerate(sortedYears):
		output.write('\n\n## ['+str(year[0])+'](/'+str(year[0])+'/README.md'+')')
		for indexM, month in enumerate(sortedMonths): 
			output.write('\n\n### ['+str(monthsIndex[month[1]])+']('+str(year[0])+'/'+str(monthsIndex[month[1]])+'/README.md'+')')
			for indexV, version in enumerate(sortedList):
				#output.write('\n# ['+ version[0]+'](\n')
				#output.write
				if version[0] == year[0] and version[1] == month[1]:
					output.write('\n- [' + str(version[2]) + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
					output.write('\n- [' + str(version[2]) + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
				else:
					continue
		

