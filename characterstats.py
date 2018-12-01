#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

import rollStats
import apiFetching
import recommendStats

def calculateStats(raceName, className):
	allStats = []

	allStats.append(recommendStats.recommend(className ,rollStats.rollStats()))
	allStats.append(apiFetching.getRace(raceName)["speed"])
	allStats.append(apiFetching.getRace(raceName)["ability_bonuses"])
	allStats.append(apiFetching.getClass(className)["hit_die"])

	return allStats