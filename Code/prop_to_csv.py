#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:03:45 2019

@author: dviryo
"""

import csv
import os
import glob
import pandas as pd
os.chdir("/home/dviryo/CompClassFall2019/assignments/prop/htmls")
from bs4 import BeautifulSoup
# In[1]:
with open('CA_all.html', 'r') as f0:
    CA_all_html = f0.read()

# In[2]:    
soup = BeautifulSoup(CA_all_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
copy = titles[:] 
from collections import Counter # Counter counts the number of occurrences of each item
from itertools import tee, count

def uniquify(seq, suffs = count(1)):
    """Make all the items unique by adding a suffix (1, 2, etc).
    `seq` is mutable sequence of strings.
    `suffs` is an optional alternative suffix iterable.
    """
    not_unique = [k for k,v in Counter(seq).items() if v>1] 
    # suffix generator dict - e.g., {'title': <my_gen>, 'anothertitle': <my_gen>}
    suff_gens = dict(zip(not_unique, tee(suffs, len(not_unique))))  
    for idx,s in enumerate(seq):
        try:
            suffix = str(next(suff_gens[s]))
        except KeyError:
            # s was unique
            continue
        else:
            seq[idx] += suffix

uniquify(copy)
   
    
details = []
for elc in soup.find_all("div", class_="divRepeaterInternal"):
        details.append(elc.text.splitlines())

clean = []
for i in details:
    i = list(filter(None, i))
    while(" " in i):
        i.remove(" ")
    while(" -" in i):
        i.remove(" -")
    clean.append(i)
    
cal_all_prop = dict(zip(copy, clean))

with open('cal_all_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_all_prop.items():
       writer.writerow([key] + cal_all_prop[key])
