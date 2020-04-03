#!/usr/bin/env python
# coding: utf-8

# Corona.py 2.0
from datetime import datetime
from bs4 import BeautifulSoup
from os import path
import os, time, requests

#Sets up the empty string to store the data.
output = ''
#Fetches and saves the current date to 'date'.
date = datetime.strftime(datetime.now(), '_%Y-%m-%d')

page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')
resultsTotal = soup.find(class_='total_row')
resultstotalList = resultsTotal.text.strip().split('\n')

output += 'Total'.center(31) + '\n' \
       + 'Confirmed'.ljust(31) + '-' + resultstotalList[1].rjust(10) + '\n' \
       + 'Recovered'.ljust(31) + '-' + resultstotalList[3].rjust(10) + '\n' \
       + 'Dead'.ljust(31)+ '-' + resultstotalList[5].rjust(10) + '\n\n'

resultsWorld = soup.find(id='main_table_countries_today')
resultsworldFine = resultsWorld.find_all('td')

resultsworldList = [x.text.strip() if x.text.strip() != '' else '0' for x in resultsworldFine]

output += 'World'.center(31) + '\n' \
       + 'Country'.ljust(31) + 'Confirmed'.rjust(10) + 'Dead'.rjust(9) + '\n'

for x in range(len(resultsworldList[1::10])-1):
    output += resultsworldList[0::10][x].ljust(31) + '-' \
           + resultsworldList[1::10][x].rjust(9) \
           + resultsworldList[3::10][x].rjust(9) + '\n'

page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
soup = BeautifulSoup(page.content, 'html.parser')
resultsUS = soup.find(id='usa_table_countries_today')
resultsusFine = resultsUS.find_all('td')

resultsusList = [x.text.strip() if x.text.strip() != '' else '0' for x in resultsusFine]

output += '\n' + 'United States'.center(31) + '\n' \
       + 'State'.ljust(31) + 'Confirmed'.rjust(10) + 'Dead'.rjust(9) + '\n'

for x in range(len(resultsusList[1::7])):
    output += resultsusList[0::7][x].ljust(31) + '-' \
           + resultsusList[1::7][x].rjust(9) \
           + resultsusList[3::7][x].rjust(9) + '\n'

#Creates folder in current working directory.
pathDir = os.path.join(os.path.expanduser('~'),'Documents','PythonPrograms', 'VirusData')
if path.exists(pathDir) == False:
    os.makedirs(pathDir)

#Joins and saves the filepath to a variable to make it easier to read code. 
filePath = os.path.join(os.path.expanduser('~'),'Documents','PythonPrograms', 'VirusData', 'Covid19' + date + '.txt')

#Creates and adds the output file to the VirusData folder and then closes.
with open(filePath, 'w') as fileW:
    fileW.write(output)