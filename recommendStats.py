def recommend(pclass,statList):
    classes = ["Cleric","Fighter","Rogue","Wizard","Barbarian","Bard","Druid","Monk","Paladin","Ranger","Sorcerer","Warlock"]
    #Stat order: Strength, Dexterity, Constitution, Intellegence, Wisdom, Charisma
    #                     Cleric         Fighter        Rogue          Wizard         Barbarian      Bard           Druid          Monk           Paladin        Ranger         Sorcerer       Warlock
    statDistributions = [ [2,5,1,3,0,4], [0,3,1,2,5,4], [5,0,3,2,4,1], [5,2,1,0,4,3], [0,2,1,5,4,3], [5,1,3,4,2,0], [2,3,1,4,0,5], [5,0,2,1,3,4], [0,4,2,5,3,1], [5,0,2,3,1,4], [5,2,1,4,3,0], [5,2,1,4,3,0] ]
    key = classes.index(pclass)
    newStatList = [0,0,0,0,0,0]
    for i in range(6):
        newStatList[statDistributions[key][i]] = statList[i]
    return newStatList