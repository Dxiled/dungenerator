def recommend(pclass,statList):
    classes = ["Cleric","Fighter","Rogue","Wizard","Barbarian","Bard","Druid","Monk","Paladin","Ranger","Sorcerer","Warlock"]
    #Stat order: Strength, Constitution, Dexterity, Intellegence, Wisdom, Charisma
    #                     Cleric         Fighter        Rogue          Wizard         Barbarian      Bard           Druid          Monk           Paladin        Ranger         Sorcerer       Warlock
    statDistributions = [ [2,1,5,3,0,4], [0,1,3,2,5,4], [5,3,0,2,4,1], [5,1,2,0,4,3], [0,1,2,5,4,3], [5,3,1,4,2,0], [2,1,3,4,0,5], [5,2,0,1,3,4], [0,2,4,5,3,1], [5,2,0,3,1,4], [5,1,2,4,3,0], [5,1,2,4,3,0] ]
    key = classes.index(pclass)
    newStatList = [0,0,0,0,0,0]
    for i in range(6):
        newStatList[statDistributions[key][i]] = statList[i]
    return newStatList