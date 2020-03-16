#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:14:09 2020

@author: rayhan, rezvan
"""

import csv
import bibtexparser
from bibtexparser.bparser import BibTexParser

parser = BibTexParser(common_strings=True,
                      ignore_nonstandard_types=True,
                      interpolate_strings=True)
parser.homogenise_fields = True


for index in range(1,2):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/sciencedirect/q13/{index}.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    #file = open(f'wiley-sm-20002020-{index}.csv', "a")
    #file.write(f'Document Title, Abstract, year, pdf Link ,label\n')
    
    with open(f'sciencedirect-q12-20002020-{index}.csv', mode='a') as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
        
        for item in bib_database.entries:
            if 'year' in item.keys() and 'abstract' in item.keys():
                file_writer.writerow([item["title"], item["abstract"] ,item["year"], item["url"] ,'no'])
            elif ('abstract' in item.keys()) and ('year' not in item.keys()):
                file_writer.writerow([item["title"], item["abstract"] ,0000, item["url"] ,'no'])
            elif ('year' in item.keys()) and ('abstract' not in item.keys()):
                file_writer.writerow([item["title"], "Nothing" ,item["year"], item["url"] ,'no'])
            else:
                file_writer.writerow([item["title"], "Nothing" ,0000, item["url"] ,'no'])

    file.close()