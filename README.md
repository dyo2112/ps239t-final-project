# ps239t-final-project

Ballot measures voting patterns project - 

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
#cleans the data
#adds variables to measure level of success
