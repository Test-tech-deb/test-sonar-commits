#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:34:57 2020

@author: rezvan
"""
import csv

for index in range(1,20):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/springerlink/{index}.csv', mode='r') as original_file:
        csv_reader = csv.DictReader(original_file)        
        
        with open(f'springer-q1-20002020-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for row in csv_reader:
                file_writer.writerow([row["Item Title"], "Nothing" ,row["Publication Year"], row["URL"] ,'no'])
                
        file.close(); 
                