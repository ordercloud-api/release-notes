import pathlib, os, glob, fnmatch, re, datetime, operator, calendar
from pathlib import Path
#import pdb

monthsIndex = {0:'January', 1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11:'December'}

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
	#print(item[0],index, item)
	if index == 0:
		sortedYears.append(item[0])
	if item[0] > sortedList[index-1][0]:
		sortedYears.append(item[0])

# add the month indexes to sortedMonths
for index, item in enumerate(sortedList):
	#print(index, item)
	if index == 0:
		sortedMonths.append([item[0], item[1]])
	elif item[1] == 'README.md':
		continue
	elif item[1] > sortedList[index-1][1]:
		sortedMonths.append([item[0], item[1]])

sortedYears = sorted(sortedYears)
sortedMonths = sorted(sortedMonths, key=operator.itemgetter(0,1))

#print(sortedYears)
#print(sortedMonths)

# write the markdown for repo readme.md
with open('README.md', 'w') as output:
	output.write('\n# OrderCloud Release Notes \n*Release notes for the OrderCloud API*')	
	#output.write(str(sortedList))
	for indexY, year in enumerate(sortedYears):
		#print(year)
		output.write('\n\n## ['+str(year)+'](/'+str(year)+'/README.md'+')')
		for indexM, month in enumerate(sortedMonths):
			#print(month) 
			if month[0] == year:
				output.write('\n\n### ['+str(monthsIndex[month[1]])+']('+str(year)+'/'+str(monthsIndex[month[1]])+'/README.md'+')')
			else:
					continue
			for indexV, version in enumerate(sortedList):
				#output.write('\n# ['+ version[0]+'](\n')
				#output.write
				if version[0] == year and version[1] == month[1]:
					output.write('\n- [' + str(version[2]) + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
					#output.write('\n- [' + str(version[2]) + '](/'+str(version[0])+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
				else:
					continue
		

# write the markdown for year readmes

for indexY, year in enumerate(sortedYears):
	with open(''+str(year)+'/README.md', 'w') as output:
		output.write('# OrderCloud API Releases for '+str(year)+'\n')
		for indexM, month in enumerate(sortedMonths):
			#print(month) 
			if month[0] == year:
					output.write('\n\n## ['+str(monthsIndex[month[1]])+']('+str(monthsIndex[month[1]])+'/README.md'+')')
			else:
					continue
			for indexV, version in enumerate(sortedList):
					#output.write('\n# ['+ version[0]+'](\n')
					#output.write
				if version[0] == year and version[1] == month[1]:
					output.write('\n- [' + str(version[2]) + ']('+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
					#output.write('\n- [' + str(version[2]) + ']('+'/'+str(monthsIndex[version[1]])+'/'+str(version[2])+')')
				else:
					continue

# write the markdown for month readmes
for year in sortedYears:
	for month in sortedMonths:
		if month[0] == year:
			with open(''+str(month[0])+'/'+str(monthsIndex[month[1]])+'/README.md', 'w') as output:
				print(month)
				output.write('# OrderCloud API Releases for '+str(monthsIndex[month[1]])+', '+str(month[0])+'\n')
				for indexV, version in enumerate(sortedList):

							#output.write('\n# ['+ version[0]+'](\n')
							#output.write
					if version[0] == year and version[1] == month[1]:

						print(version)
						output.write('\n- [' + str(version[2]) + ']('+'/'+str(version[2])+')')
						#output.write('\n- [' + str(version[2]) + ']('+'/'+str(version[2])+')')
					else:
							continue
