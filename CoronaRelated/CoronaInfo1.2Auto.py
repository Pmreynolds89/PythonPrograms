#!/usr/bin/env python
# coding: utf-8

# Corona.py 1.2
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from os import path
import re, os, time

def convertTuple(tup):  # Tuple > String converter.
    str = ''.join(tup)
    return str

# Function to process a single URL.
def my_url_function(url):
    global data, data2, data3 # Loads variables to be written to the nonfucntion variables
    
    options = Options()     # Adding option to remove program from launching a browser
    options.headless = True 
    
    # Starts firefox and gets URL.
    # Adds options to remove headless, removes gecko spitting out a log, and directs to gecko.
    driver = webdriver.Firefox( 
        options=options, service_log_path=os.devnull, executable_path=r'C:\Users\Vehem\Anaconda3\geckodriver.exe')
    driver.get(url)
    
    # Filters URLs to the correct block to execute.
    if url == 'https://www.coronatracker.com/analytics/':
        elem = driver.find_elements_by_xpath(                                # Directs to the overall cases table.
            r'/html/body/div[1]/div/div/div[4]/div[2]/div[2]/div[1]/div[1]')
        elem2 = driver.find_elements_by_xpath(                               # Directs to the table for countries effected.
            r'/html/body/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody')
        # Both of these convert the object to readable text.
        elem = elem[0].text    
        elem2 = elem2[0].text 
        # Splits string to a list.
        data = elem.split('\n')
        # Same - (If a lc letter is followed by a space | space followed by a num.)
        data2 = re.split(r'(?<![a-z])\s|\s(?=\d)', elem2)

    if url == 'https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html':
        button = driver.find_element_by_xpath(
            '/html/body/div[1]/main/article/section/div/div/div[4]/div/button')
        driver.execute_script("arguments[0].click();", button)
        elem3 = driver.find_elements_by_xpath(                               # Directs to the table for states effected.
            r'/html/body/div[1]/main/article/section/div/div/div[4]/div/table/tbody')
        elem3 = elem3[0].text                                                #Converts object to a readable text.
        data3 = re.split(r'(?<![a-z])\s|\s(?=\d)', elem3)
    driver.close()

# Global variables to store data from my_url_function to be processed below.
urls  = ['https://www.coronatracker.com/analytics/', 
         'https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html']
data  = []
data2 = []
data3 = []
vOmega = ()
date = datetime.strftime(datetime.now(), '_%Y-%m-%d')#Fetches and saves the current date to 'date'.

print('Retrieving data...')
#Main loop that feeds both URLs into the url function to gather data.
for i_url in urls:         
    my_url_function(i_url)
print('Organizing data...')
# Organizes text for the data variable. Set to run half the length.
for x in range(len(data[1::2])):
    vOmega += (data[::2][x].ljust(16), '-',   # Index 0 then every 2 indexes.
               data[1::2][x].rjust(8), '\n')  # Index 1 then every 2 indexes.

vOmega += ('\n', 'Country'.ljust(23), 'Confirmed'.ljust(10),  # Adds a tuple to vOmega to describe list below.
           'Recovered'.ljust(11), 'Dead'.ljust(1), '\n')

# Organizes text for the data2 variable. Set to run 1/4th the length.
for x in range(len(data2[1::4])):
    vOmega += (data2[::4][x].ljust(23), '-',  # Index 0 then every 4 indexes.
               data2[1::4][x].rjust(8),       # Index 1 then every 4 indexes.
               data2[2::4][x].rjust(8),       # Index 2 then every 4 indexes.
               data2[3::4][x].rjust(8), '\n') # Index 3 then every 4 indexes.
    
vOmega += ('\n', 'State'.ljust(23), 'Confirmed'.center(14),  # Adds a tuple to vOmega to describe list below.
            'Dead'.ljust(1), '\n') 

# Organizes text for the data 3 variable. Set to run 1/3rd the length.    
for x in range(len(data3[1::3])):
    vOmega += (data3[::3][x].ljust(23), '-',  # Index 0 then every 3 indexes.
               data3[1::3][x].rjust(8),       # Index 1 then every 3 indexes.
               data3[2::3][x].rjust(8), '\n') # Index 2 then every 3 indexes.
    
# Converts the vOmega tuple to string to output.
strData = convertTuple(vOmega)

#Creates folder in current working directory
pathDir = os.path.join(os.path.expanduser('~'),'Documents','PythonPrograms', 'VirusData')
if path.exists(pathDir) == False:
    os.makedirs(pathDir)

filePath = os.path.join(os.path.expanduser('~'),'Documents','PythonPrograms', 'VirusData', 'Covid19' + date + '.txt')
print('Saving data to file...')
#Creates and adds the output file to the VirusData folder and then closes.
with open(filePath, 'w') as fileW:
    fileW.write(strData)
print('Done!')   
time.sleep(2.4)