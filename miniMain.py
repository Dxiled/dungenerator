import characterstats
import generate

def miniMain():
	className = generate.pclass()
	raceName = generate.rc()


	stats =  characterstats.calculateStats(raceName, className)

	print(generate.intro(generate.adj(), raceName, className, generate.loc(), generate.bstory()))
	print("Your stats are:")
	print("Attributes:" + str(stats[0]) + " Speed:" + str(stats[1]) + " Ability bonuses:" + str(stats[2]) +" Hit die:" + str(stats[3]))

miniMain()