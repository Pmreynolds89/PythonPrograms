#!/usr/bin/env python
# coding: utf-8

import os


def Respec(name):
    fileSave = os.path.join(
        os.path.expanduser('~'), 'Documents', 'Mount&Blade Warband',
                                 'Characters', 'Blank Characters',  name[56:])
    fileDir = os.path.join(
        os.path.expanduser('~'), 'Documents',  'Mount&Blade Warband',
                                 'Characters', 'Blank Characters')
    if os.path.exists(fileDir) is False:
        os.makedirs(fileDir)

    # Opens the files for read only, stores data to a variable and then closes.
    with open(name, 'r') as characterFile:
        char = characterFile.readlines()

    # Format text.
    charStrip = [x.strip() for x in char if x.strip()]
    charSplit = [x.split(' = ') for x in charStrip]
    # Create 2 lists.
    key = [x[0] for x in charSplit]
    value = [x[1] if x[1].isdigit() is not True
             else int(x[1]) for x in charSplit]
    # Create a dictionary with the 2 lists.
    charDict = dict(zip(key, value))

    # Sums attributes and adds to values[4], then sets all relative
    # values in value to 0. Attribute points.
    value[4] = charDict['attribute_points'] + sum(value[7:11])
    removeSP = value[9]
    for x in range(len(value[7:11])):
        value[x+7] = 0

    # Sums skills and adds to value[5], then sets all relative values
    # in key to 0. Skill points. Removes Int; int gives 1 SP on selection.
    value[5] = charDict['skill_points'] + sum(value[11:53]) - removeSP
    for x in range(len(value[11:53])):
        value[x+11] = 0

    # Combines updated key and value list into a new dictionary.
    charDictEnd = dict(zip(key, value))

    charOut = ''
    for ind, x in enumerate(charDictEnd):
        if (ind == 4 or ind == 7 or ind == 11 or ind == 53 or ind == 60):
            charOut += '\n'
        charOut += f'{x} = {str(charDictEnd[x])}\n'

    # Saves the text to a file, identical to the input.
    with open(fileSave, 'w') as fileW:
        fileW.write(charOut)


fileIn = os.path.join(
    os.path.expanduser('~'), 'Documents', 'Mount&Blade Warband', 'Characters')

for dirpath, dirnames, filenames in os.walk(fileIn):
    for x in filenames:
        fp = os.path.join(fileIn, x)
        Respec(fp)
