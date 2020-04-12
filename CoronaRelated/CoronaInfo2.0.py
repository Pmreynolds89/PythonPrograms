#!/usr/bin/env python
# coding: utf-8

# Corona.py 2.0d
from datetime import datetime
from bs4 import BeautifulSoup
from os import path
import os, time, requests

#Sets up the empty string to store the data.
output = ''
#Fetches and saves the current date to 'date'.
date = datetime.strftime(datetime.now(), '_%Y-%m-%d')

#Soup collects the html data of a site, only stores the class data for world totals, and then splits the data into a list.
print('Retrieving data...')
page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')

#Soup finds and stores the class data for country totals.
resultsWorld = soup.find(id='main_table_countries_today')
resultsworldFine = resultsWorld.find_all('td')
#Counts the number of headers and saves the amount to countSumW; the headers represent different categories for each country.
countW = resultsWorld.find_all('th')
countSumW = len(countW)

#Strips the text and adds zeros where data is missing. Then removes irrelevant data before and after.
resultsworldText = [x.text.strip() if x.text.strip() != '' else '0' for x in resultsworldFine]
resultsworldList = resultsworldText[resultsworldText.index('USA'):resultsworldText.index('Total:')]

#Formats the world totals and adds them to a string variable to save to a .txt file.
resultstotalList = resultsworldText[resultsworldText.index('World'):resultsworldText.index('All')]
output += 'Total'.center(31) + '\n' \
       + 'Confirmed'.ljust(31) + '-' + resultstotalList[1].rjust(10) + '\n' \
       + 'Recovered'.ljust(31) + '-' + resultstotalList[5].rjust(10) + '\n' \
       + 'Dead'.ljust(31)+ '-' + resultstotalList[3].rjust(10) + '\n\n'


#Adds headers for the upcoming country totals and adds them to the string variable.
output += 'World'.center(31) + '\n' \
       + 'Country'.ljust(31) + 'Confirmed'.rjust(10) + 'Dead'.rjust(9) + '\n'

#Formats the country totals and adds them to the string variable.
for x in range(len(resultsworldList[::countSumW])):
    output += resultsworldList[0::countSumW][x].ljust(31) + '-' \
           + resultsworldList[1::countSumW][x].rjust(9) \
           + resultsworldList[3::countSumW][x].rjust(9) + '\n'

#Soup finds and stores the id data for states in the United States.
page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
soup = BeautifulSoup(page.content, 'html.parser')
resultsUS = soup.find(id='usa_table_countries_today')
resultsusFine = resultsUS.find_all('td')
#Counts the number of headers and saves the amount to countSumU; the headers represent different categories for each state.
countU = resultsUS.find_all('th')
countSumU = len(countU)

#Strips the text and adds zeros where data is missing.    
resultsusList = [x.text.strip() if x.text.strip() != '' else '0' for x in resultsusFine]

#Adds headers to the upcoming state totals and adds them to the string variable.
output += '\n' + 'United States'.center(31) + '\n' \
       + 'State'.ljust(31) + 'Confirmed'.rjust(10) + 'Dead'.rjust(9) + '\n'

#Formats the state totals and adds them to the string variable.
for x in range(1, len(resultsusList[::countSumU])):
    output += resultsusList[0::countSumU][x].ljust(31) + '-' \
           + resultsusList[1::countSumU][x].rjust(9) \
           + resultsusList[3::countSumU][x].rjust(9) + '\n'

#Creates folder in current working directory.
pathDir = os.path.join('.','VirusData')
if path.exists(pathDir) == False:
    os.makedirs(pathDir)

#Joins and saves the filepath to a variable.
filePath = os.path.join('.', 'VirusData', 'Covid19' + date + '.txt')

print('Saving data to file...')
#Creates and adds the output file to the VirusData folder and then closes.
with open(filePath, 'w') as fileW:
    fileW.write(output)
print('Done!')   
time.sleep(2.4)