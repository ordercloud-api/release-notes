import pathlib, os, glob, fnmatch, re, datetime, operator, calendar
from pathlib import Path

# made by klreeher; auto generates repo, year, and month readmes based off of file system
# if the month doesn't exist or the version doesn't exist, it won't get generated here

monthsIndex = {0:'January', 1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11:'December'}

versions = glob.glob('**/20??/*/v*.md', recursive = True)

sortedList = []
sortedMonths = []
sortedVersions = []
sortedYears = []

for filename in versions:
	filename = filename.split('\\')
	sortedList.append(filename)

# replace month name with month value for sorting
for k, v in monthsIndex.items():
	for item in sortedList:
		if item[1] == v:
			item[1]=k


# sorts everything all nice (DOES NOT WORK IF REVERSE SORTED)
sortedList = sorted(sortedList, key=operator.itemgetter(0,1))

# add the year indexes to sortedYears
for index, item in enumerate(sortedList):
	if index == 0:
		sortedYears.append(item[0])
	if item[0] > sortedList[index-1][0]:
		sortedYears.append(item[0])

# add the month indexes to sortedMonths
for index, item in enumerate(sortedList):
	if index == 0:
		sortedMonths.append([item[0], item[1]])
	elif item[1] == 'README.md':
		continue
	elif item[1] > sortedList[index-1][1]:
		sortedMonths.append([item[0], item[1]])

sortedYears = sorted(sortedYears, reverse=True)
sortedMonths = sorted(sortedMonths, key=operator.itemgetter(0,1), reverse=True)

# write the markdown for repo readme.md
with open('README.md', 'w') as output:
	output.write('\n# OrderCloud Release Notes \n*Release notes for the OrderCloud API*\n\n')	
	output.write('| Released | Versions |\n|---|---|')	#output.write(str(sortedList))
	for indexY, year in enumerate(sortedYears):
		#print(year)
		output.write('\n| | |')
		for indexM, month in enumerate(sortedMonths):
			#print(month) 
			if month[0] == year:
				output.write('\n| ['+str(year)+'](/'+str(year)+'/README.md'+') ['+str(monthsIndex[month[1]])+']('+str(monthsIndex[month[1]])+'/README.md'+') |')
			else:
					continue
			for indexV, version in enumerate(sortedList):
				#output.write('\n# ['+ version[0]+'](\n')
				#output.write
				if version[0] == year and version[1] == month[1]:
					# you're going to have to change the string index on version > 99
					output.write(' [1.0.' + str(version[2])[1:3] + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
					#output.write('\n- [' + str(version[2]) + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
				else:
					continue
			output.write(' |')
		

# write the markdown for year readmes

for indexY, year in enumerate(sortedYears):
	with open(''+str(year)+'/README.md', 'w') as output:
		output.write('# OrderCloud API Releases for '+str(year)+'\n')
		output.write('| Released | Versions |\n|---|---|')
		for indexM, month in enumerate(sortedMonths):
			if month[0] == year:
					output.write('\n| ['+str(monthsIndex[month[1]])+']('+str(monthsIndex[month[1]])+'/README.md'+') |')
			else:
					continue			
			#print(indexM, month)
			#output.write('')
			for indexV, version in enumerate(sortedList):
				if version[0] == year and version[1] == month[1]:
						output.write(' [1.0.' + str(version[2])[1:3] + ']('+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+') ')
				else:
					continue
			output.write(' |')

				
# write the markdown for month readmes
for year in sortedYears:
	for month in sortedMonths:
		if month[0] == year:
			with open(''+str(month[0])+'/'+str(monthsIndex[month[1]])+'/README.md', 'w') as output:
				output.write('# OrderCloud API Releases for '+str(monthsIndex[month[1]])+', '+str(month[0])+'\n')
				for indexV, version in enumerate(sortedList):
					if version[0] == year and version[1] == month[1]:
						output.write('\n- [1.0.' + str(version[2])[1:3] + ']('+str(version[2])+')')
					else:
							continue
