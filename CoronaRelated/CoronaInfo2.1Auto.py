#!/usr/bin/env python
# coding: utf-8

# Corona.py 2.1
from datetime import datetime
from bs4 import BeautifulSoup
from os import path
import pandas as pd
import os
import requests


# Fetches and saves the current date to 'date'.
date = datetime.strftime(datetime.now(), '%m_%d_%Y')

# Soup collects the html data of a site, only stores the class data for world
# totals, and then splits the data into a list.
page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')

# Soup finds and stores the class data for country totals.
resultsWorld = soup.find(id='main_table_countries_today')
resultsworldFine = resultsWorld.find_all('td')
# Counts the number of headers and saves the amount to countSumW; the headers
# represent different categories for each country.
countW = resultsWorld.find_all('th')
countSumW = len(countW)

# Strips the text and adds zeros where data is missing. Then removes irrelevant
# data before and after. Removes extra characters from the number strings.
# Converts the number strings to integers.
resultsworldText = [
    x.text.strip() if x.text.strip() != '' else '0'for x in resultsworldFine]
resultsworldList = resultsworldText[
    resultsworldText.index('World'):resultsworldText.index('Total:')]
resultsworldList = [
    x.strip('+').replace(',','') for x in resultsworldList]
resultsworldList = [
    x if x.isdigit() is False else int(x) for x in resultsworldList]

# Creates a dictionary to store the country data.
contDict = {'Country':'','Confirmed':'','Dead':'','Date':date}
contDict['Country'] = resultsworldList[0::countSumW]
contDict['Confirmed'] = resultsworldList[1::countSumW]
contDict['Dead'] = resultsworldList[3::countSumW]

# Soup finds and stores the id data for states in the United States.
page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
soup = BeautifulSoup(page.content, 'html.parser')
resultsUS = soup.find(id='usa_table_countries_today')
resultsusFine = resultsUS.find_all('td')
# Counts the number of headers and saves the amount to countSumU;
# the headers represent different categories for each state.
countU = resultsUS.find_all('th')
countSumU = len(countU)

# Strips the text and adds zeros where data is missing.  
# Removes extra characters from the number strings.
# Converts the number strings to integers.
resultsusList = [
    x.text.strip() if x.text.strip() != '' else '0' for x in resultsusFine[countSumU:-countSumU]]
resultsusList = [
    x.strip('+').replace(',','') for x in resultsusList]
resultsusList = [
    x if x.isdigit() is False else int(x) for x in resultsusList]

# Creates a dictionary that stores the US data.
usDict ={'State':'', 'Confirmed':'', 'Dead':'','Date':date}
usDict['State'] = resultsusList[0::countSumU]
usDict['Confirmed'] = resultsusList[1::countSumU]
usDict['Dead'] = resultsusList[3::countSumU]

# Creates folder in a specified folder.
pathDir = os.path.join(
    os.path.expanduser('~'), 'Documents', 'PythonPrograms_Local', 'VirusData')
if path.exists(pathDir) is False:
    os.makedirs(pathDir)

# Joins and saves the filepaths to variables.
contFP = os.path.join(
    os.path.expanduser('~'), 'Documents', 'PythonPrograms_Local',
    'VirusData', 'Covid19_Countries.csv')
usFP = os.path.join(
    os.path.expanduser('~'), 'Documents', 'PythonPrograms_Local',
    'VirusData', 'Covid19_USA.csv')

# Converts dictionaries to data frames and saves them as csv files.
# Sorts country data by the Confirmed column and resets index.
contDF = pd.DataFrame(contDict)
contDF.sort_values('Confirmed', ascending = False, ignore_index = True, inplace = True)
contDF.to_csv(contFP, mode='a')

usDF = pd.DataFrame(usDict)
usDF.to_csv(usFP, mode='a')