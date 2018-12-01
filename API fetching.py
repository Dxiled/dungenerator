import urllib.request
import ast

def readAPI(sublist):
	response = urllib.request.urlopen("http://dnd5eapi.co/api/" + sublist)
	html = response.readline()  # reads one line

	data = ast.literal_eval(html.decode('utf-8'))

	return data

'''
Get info of the race by their name
returns the api's result as a dictionary
'''
def getRace(raceName):
	raceName = raceName.lower()

	raceIndex = {'dwarf':1,
				 'elf':2,
				 'halfling':3,
				 'human':4,
				 'dragonborn':5,
				 'gnome':6,
				 'half-elf':7,
				 'half-orc':8,
				 'teifling':9
	}

	raceData = readAPI('races/' + str(raceIndex[raceName]))

	return raceData

'''
Get class information from API
for some reason you can use the class name instead of its index and it still works
'''
def getClass(className):
	className = className.lower()

	classData = readAPI('classes/' + className)

	return classData

