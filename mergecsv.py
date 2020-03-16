#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:26:45 2020

@author: rezvan
"""

from os import walk
import csv

csvfilelist = []
csvfilelistwithoutabstract = []

papertitlelist = []
papertitlelistwithoutabstract = []

##############
for (dirpath, dirnames, filenames) in walk('/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files with abstract'):
    csvfilelist.extend(filenames)
    break

for (dirpath, dirnames, filenames) in walk('/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files'):
    csvfilelistwithoutabstract.extend(filenames)
    break

############## csv files with abstract
count = 0

for file in csvfilelist:
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files with abstract/' + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'{row[0]}')
                papertitlelist.append(row[0].strip().lower())
                line_count += 1
        count += line_count

uniquePaperTitleList = set(papertitlelist)

uniques = dict((keys,0) for keys in uniquePaperTitleList)

f_file = open(f'papers_abstract.csv', mode='a')
file_writer = csv.writer(f_file, delimiter=',')
file_writer.writerow(['Document Title', 'Abstract', 'Year', 'PDF Link' ,'label'])


for file in csvfilelist:
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files with abstract/' + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0
        next(csv_reader)
        for row in csv_reader:
            if(uniques[row[0].strip().lower()] == 0):
                if(row[1] != "Nothing"):
                    file_writer.writerow(row)
                else:
                    file_writer.writerow([row[0], " " ,row[2], row[3] ,row[4]])
                uniques[row[0].strip().lower()] = 1
                
f_file.close()

############### csv files
count = 0

for file in csvfilelist:
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files/' + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'{row[0]}')
                papertitlelistwithoutabstract.append(row[0].strip().lower())
                line_count += 1
        count += line_count

uniquePaperTitleListwithoutabstract = set(papertitlelistwithoutabstract)

uniqueswithout = dict((keys,0) for keys in uniquePaperTitleListwithoutabstract)


f_file = open(f'papers.csv', mode='a')
file_writer = csv.writer(f_file, delimiter=',')
file_writer.writerow(['Document Title', 'Abstract', 'Year', 'PDF Link' ,'label'])


for file in csvfilelist:
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files/' + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0
        next(csv_reader)
        for row in csv_reader:
            if(uniqueswithout[row[0].strip().lower()] == 0):
                if((row[0].strip().lower(),1) not in uniques):
                    if(row[1] != "Nothing"):
                        file_writer.writerow(row)
                    else:
                        file_writer.writerow([row[0], " " ,row[2], row[3] ,row[4]])
                uniqueswithout[row[0].strip().lower()] = 1
                
f_file.close()