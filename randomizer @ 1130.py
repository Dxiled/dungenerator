import random

def randomize_stats():
    stat_list1 = []
    for stat1 in range(4):
        stat_list1.append(random.randint(1,6))
    stat_list1.remove(min(stat_list1))
    stat1 = sum(stat_list1)
    print('Your first stat is', stat1)

    stat_list2 = []
    for stat2 in range(4):
        stat_list2.append(random.randint(1,6))
    stat_list2.remove(min(stat_list2))
    stat2 = sum(stat_list2)
    print('Your second stat is', stat2)

    stat_list3 = []
    for stat3 in range(4):
        stat_list3.append(random.randint(1,6))
    stat_list3.remove(min(stat_list3))
    stat3 = sum(stat_list3)
    print('Your third stat is', stat3)

    stat_list4 = []
    for stat4 in range(4):
        stat_list4.append(random.randint(1,6))
    stat_list4.remove(min(stat_list4))
    stat4 = sum(stat_list4)
    print('Your fourth stat is', stat4)

    stat_list5 = []
    for stat5 in range(4):
        stat_list5.append(random.randint(1,6))
    stat_list5.remove(min(stat_list5))
    stat5 = sum(stat_list5)
    print('Your third stat is', stat5)

    stat_list6 = []
    for stat6 in range(4):
        stat_list6.append(random.randint(1,6))
    stat_list6.remove(min(stat_list6))
    stat6 = sum(stat_list6)
    print('Your fourth stat is', stat6)
    

    

    stat_list = []
    stat_list.append(stat1)
    stat_list.append(stat2)
    stat_list.append(stat3)
    stat_list.append(stat4)
    stat_list.append(stat5)
    stat_list.append(stat6)
    print('\nYour list of stats is:', stat_list)

    return stat_list
    
    



def assign_stats(stats):
    print('Remember that the first stat is found in position 0.')

    print('\nEnter the position of your desired Strength stat: ')
    strength_position = int(input('Please enter the stat\'s position: '))
    strength = stats.pop(strength_position)
    print('Your Strength stat is now:', strength)
    print('\nYour remaining stats are:', stats, '\n')

    print('\nEnter the position of your desired Charisma stat: ')
    charisma_position = int(input('Please enter the stat\'s position: '))
    charisma = stats.pop(charisma_position)
    print('Your Charisma stat is now:', charisma)
    print('\nYour remaining stats are:', stats, '\n')

    print('\nEnter the position of your desired Dexterity stat: ')
    dexterity_position = int(input('Please enter the stat\'s position: '))
    dexterity = stats.pop(dexterity_position)
    print('Your Charisma stat is now:', dexterity)
    print('\nYour remaining stats are:', stats, '\n')

    print('\nEnter the position of your desired Consitution stat: ')
    constitution_position = int(input('Please enter the stat\'s position: '))
    constitution = stats.pop(constitution_position)
    print('Your Strength stat is now:', constitution)
    print('\nYour remaining stats are:', stats, '\n')

    print('\nEnter the position of your desired Wisdom stat: ')
    wisdom_position = int(input('Please enter the stat\'s position: '))
    wisdom = stats.pop(wisdom_position)
    print('Your Wisdom stat is now:', wisdom)
    print('\nYour remaining stats are:', stats, '\n')

    print('\nEnter the position of your desired Intelligence stat: ')
    intelligence_position = int(input('Please enter the stat\'s position: '))
    intelligence = stats.pop(intelligence_position)
    print('Your Intelligence stat is now:', intelligence)
    print('\nYour remaining stats are:', stats, '\n')


def main():
    stats = randomize_stats()
    assign_stats(stats)

main()
    

    
