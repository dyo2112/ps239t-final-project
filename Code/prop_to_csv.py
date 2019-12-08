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


with open('CJ1.html', 'r') as f:
    CJ_html = f.read()
    
with open('labor1.html', 'r') as f1:
    labor_html = f1.read()

with open('trans1.html', 'r') as f2:
    trans_html = f2.read()

with open('health1.html', 'r') as f3:
    health_html = f3.read()
    

with open('tax_rev1.html', 'r') as f4:
    taxrev_html = f4.read()
    

with open('natural_res1.html', 'r') as f5:
    natres_html = f5.read()
    

with open('military_vet1.html', 'r') as f6:
    milvet_html = f6.read()
# In[2]:    
soup = BeautifulSoup(CJ_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_CJ_prop = dict(zip(titles, clean))

with open('cal_CJ_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_CJ_prop.items():
       writer.writerow([key] + cal_CJ_prop[key])
       
# In[3]:
soup = BeautifulSoup(health_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_health_prop = dict(zip(titles, clean))

with open('cal_health_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_health_prop.items():
       writer.writerow([key] + cal_health_prop[key])
 
# In[4]:
soup = BeautifulSoup(labor_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_labor_prop = dict(zip(titles, clean))

with open('cal_labor_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_labor_prop.items():
       writer.writerow([key] + cal_labor_prop[key])

# In[5]:
soup = BeautifulSoup(trans_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_trans_prop = dict(zip(titles, clean))

with open('cal_trans_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_trans_prop.items():
       writer.writerow([key] + cal_trans_prop[key])
# In[6]:    
soup = BeautifulSoup(taxrev_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_taxrev_prop = dict(zip(titles, clean))

with open('cal_taxrev_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_taxrev_prop.items():
       writer.writerow([key] + cal_taxrev_prop[key])
# In[7]:    
soup = BeautifulSoup(natres_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_natres_prop = dict(zip(titles, clean))

with open('cal_natres_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_natres_prop.items():
       writer.writerow([key] + cal_natres_prop[key])
# In[8]:    
soup = BeautifulSoup(milvet_html, "html.parser")

titles = []
for tit in soup.find_all("div", class_="divRepeaterTitle"):
    titles.append(tit.text)
    
    
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
    
cal_milvet_prop = dict(zip(titles, clean))

with open('cal_milvet_prop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in cal_milvet_prop.items():
       writer.writerow([key] + cal_milvet_prop[key])

# In[999]:    
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
