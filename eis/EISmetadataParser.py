# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:18:10 2016

@authors: madeleine bonsma, adrian d'alessandro

Description: This script uses EIS report IDs from a csv version 
of the EIS database to access the metadata for each 
EIS report, scrape it, and save as one csv for the entire database. 

EIS report database: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search/search#results
Sample CSV with EIS url IDs: https://gist.github.com/wdenton/7d4b9d064d2881cca7dbf8c743f306a8
Or: https://github.com/titaniumbones/eot-sprint-toolkit/blob/master/eis/1-EIS-ID/eis-listing.csv

---------

Usage: python EISmetadataParser.py <path-to-inputcsv> <output_filename>
Example usage: python EISmetadataParser.py eis-listing.csv metadata.csv

---------

Installing Python:
- download and install Anaconda for your operating system (Python 3 is recommended) at this link:
 https://www.continuum.io/downloads
Anaconda contains Python, many common Python libraries, an IDE (Spyder)
and a command prompt (conda prompt).

Python libraries required:
- csv
- os
- sys
- urllib3
- BeautifulSoup

If any libraries are missing, run the following in the command prompt:
 pip install <libraryname>
 Example: pip install BeautifulSoup
 
Note: if using Windows, you'll need to use something other than the regular Windows command prompt. 
I recommend using conda prompt, included if you used Anaconda to get Python, or Git Bash.

Running this script:
1. open conda prompt
2. type this command: python EISmetadataParser.py <path-to-inputcsv> <output_filename>
Example command: python EISmetadataParser.py 1-EIS-ID/eis-listing.csv metadata.csv

Note: the input csv should have the EIS IDs (found at the end of each EIS url) as the first column. 
This will become the first column of the output csv as well.

TO DO:
 - check if there are more or less header categories on a page than expected, if there are, return a warning
 - check if a row is already in the csv before adding it again
 - add column(s) in csv with link to pdf(s) in EIS report 
 - figure out how to do https securely?

"""

import csv
import os.path
import sys

# ------------------ functions --------------------

def url_to_divs(url):
    """
    This function takes a url (example: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=223815)
    and collects all the items that are of class "form-item" - this is the metadata we want.
    """
    import urllib3
    from bs4 import BeautifulSoup

    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data, "lxml")
    
    mydivs = soup.findAll("div", { "class" : "form-item" })
    return mydivs

# ------------------------------------------------------------

# url for the ESI metadata page, minus the specific ID
base_url = "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId="

csv_with_ids = sys.argv[1]
outfile = sys.argv[2]

# loop through scraped list of EIS reports and collect IDs for urls
id_list = []
with open(csv_with_ids, "rb") as input_file:
    reader = csv.reader(input_file, delimiter=',')
    for row in reader:
        try:
            ID = int(row[0])
            id_list.append(ID)
        except:
            continue

# loop through IDs and scrape metadata
for ID in id_list:
    url = base_url + str(ID)
    
    mydivs = url_to_divs(url) # object that contains all metadata
    
    fields_list = []
    
    # loop through each field and get a list of items
    for div in mydivs:
        fields = [x for x in div]
        fields_list.append(fields)
                
    # separate into headers and data
    headers = ["EIS url ID"]
    info = [ID]
    for i in fields_list:
        headers.append(i[1].text)
        info.append(i[2].replace('\t',"").replace('\n',"")) #strip all extra tabs and newlines

    # check if output file exists:
    if os.path.isfile(outfile) == True:
        exists = True
    else:
        exists = False
    
    # write data to file
    with open(outfile, "ab") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if exists == False: # write header if this is the first time through
            writer.writerow(headers)         
        writer.writerow(info)
            