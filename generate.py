from random import *
import WTF

def adj():
    adjective = WTF.adjectives[randint(0,len(WTF.adjectives)-1)]
    return adjective

def rc():
    race = WTF.race[randint(0,len(WTF.race)-1)]
    return race

def pclass():
    dclass = WTF.dclass[randint(0,len(WTF.dclass)-1)]
    return dclass

def loc():
    location = WTF.location[randint(0,len(WTF.location)-1)]
    return location

def bstory():
    backstory = WTF.backstory[randint(0,len(WTF.backstory)-1)]
    return backstory

def intro(a,r,c,l,b):
    sentence = "You're a %s %s %s from %s who %s."%(a,r,c,l,b)
    return sentence

