def racialBonuses(pclass,race,stats):
    races = ["Dragonborn","Dwarf","Elf","Gnome","Half-elf","Half-orc","Halfling","Human","Tiefling"]
    if race == "Dragonborn":
        stats[0] += 2
        stats[5] += 1
    elif race == "Dwarf":
        stats[1] += 2
    elif race == "Elf":
        stats[2] += 2
    elif race == "Gnome":
        stats[3] += 2
    elif race == "Half-elf":
        stats[5] += 2
    elif race == "Half-orc":
        stats[0] += 2
        stats[1] += 1
    elif race == "Halfling":
        stats[2] += 2
    elif race == "Human":
        for stat in stats:
            stat += 1
    else:
        stats[3] += 1
        stats[5] += 2

def subraces(race,stats):
    #STUB