#!/usr/bin/env python
# coding: utf-8

from os import path
import os


fileIn = os.path.join(
    os.path.expanduser('~'),'Documents','Mount&Blade Warband', 'Characters')

def Respec(name):

    fileSave = os.path.join(
        os.path.expanduser('~'),'Documents','Mount&Blade Warband', 'Characters','Blank Characters',  name[56:])
    fileDir = os.path.join(
        os.path.expanduser('~'),'Documents','Mount&Blade Warband', 'Characters','Blank Characters')
    if path.exists(fileDir) == False:
        os.makedirs(fileDir)
    
    #Opens the files for read only, stores data to a variable and then closes.
    with open(name, 'r') as characterFile:
        char = characterFile.readlines()

    #Format text.   
    charStrip = [x.strip() for x in char if x.strip()]
    charSplit = [x.split(' = ') for x in charStrip]
    #Create 2 lists.
    key = [x[0] for x in charSplit]
    value = [x[1] if x[1].isdigit() != True else int(x[1]) for x in charSplit]
    #Create a dictionary with the 2 lists.
    charDict = dict(zip(key, value))

    #Sums attributes and adds to 'attribute_points', then sets all relative values in value to 0.
    att_total = charDict['attribute_points'] + sum(value[7:11])
    value[4] = att_total
    for x in range(len(value[7:11])):
        value[x+7] = 0

    #Sums skills and adds to 'skill_points', then sets all relative values in key to 0.
    skill_total = charDict['skill_points'] + sum(value[11:53])
    value[5] = skill_total
    for x in range(len(value[11:53])):
        value[x+11] = 0

    #Combines updated key and value list into a new dictionary.
    charDictEnd = dict(zip(key, value))

    #Burn this part with fire.
    count = 0
    charOut = ''
    for x in charDictEnd:
        if count == 4:
            charOut += '\n'
        elif count == 7:
            charOut += '\n'
        elif count == 11:
            charOut += '\n'
        elif count ==53:
            charOut += '\n'
        elif count ==60:
            charOut += '\n'
        charOut += (str(x) + ' = '+ str(charDictEnd[x])) + '\n'
        count += 1

    #Throws the file out and forgets about it.
    with open(fileSave, 'w') as fileW:
        fileW.write(charOut)

for dirpath, dirnames, filenames in os.walk(fileIn):
    for x in filenames:
        fp = os.path.join(fileIn, x)
        Respec(fp)