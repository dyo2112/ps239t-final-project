# ps239t-final-project

Ballot measures voting patterns project - 

Short Description:

I scraped NCSL's Ballot Measure DB. Then, in R, I cleaned the data and added variables to measure the level of ballot measure success per topic and per type.

Dependencies:

R, 3.6.1
Python, 3.7.3

Files:

California Ballot Measures.pdf: My talk slides.

Code/
01_prop_to_csv.py: Scrapes the HTML from NCSL and exports to CSV.

02_gen_raw_data_knit.Rmd: generates and saves raw data.

03_clean_newdata_knit.Rmd: Loads, cleans, and adds variables to the data. Also conducts descriptive analysis of the data, producing the tables and visualizations.


Data/
CA_all.html: the DB downloaded from NCSL using the SingleFile chrome extension.

cal_prop_all.csv: Includes all the California initiatives, with observations for the following variables:

election: general/primary/special;
year;
type: initiative/leg referendun/ pop referendum;
topic: one of 39 topics categorized by NCSL;
percent: the percent yes vote on the measure;
status: pass/fail;

cal_propall_data.RData: the same as the csv.

cal_pro_pall_clean.RData: the final data file used for analysis.


Results/
change_over_time.png: change in level of success over time per topic.

iniative_vs_referendum.png: difference between level of success of initiative vs. referendum per topic.

iniative_vs_referendum2.png: comparison of success between topics per type.

overwhelming_compare.png: comparison between overwhelming success (>70% yes vote) and failure (<30% yes vote) per topic.

pass_vs_fail.png: comparison between levels of success (>50% yes vote = pass) per topic.



collecting data procees:

1. Using SingleFile chrome extension download HTML files of results from:
http://www.ncsl.org/research/elections-and-campaigns/ballot-measures-database.aspx

2. Store HTML in "htmls" folder
"CA_all.html"

3. In python, scrape the HTML into a dictionary and then save it as "cal_all_prop.csv"
Run "prop_to_csv.py"

[Here I manually fixed some data issues that I found through a QA process with Ballotpedia]

4. In R - run "gen_raw_data_knit.rmd"
It reads the csv, saves raw data into "../data/raw" folder, and data into "../data" folder.

5. run "clean_newdata_knit.rmd"
cleans the data
adds variables to measure level of success
