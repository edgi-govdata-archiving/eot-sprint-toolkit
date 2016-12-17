# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:18:10 2016

@author: madeleine
"""
import csv

base_url = "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId="

#ID = 223815
id_list = []
with open("eis-sample-page-1.csv", "rb") as input_file:
        
    

url = base_url + str(id)
    

def url_to_divs(url):
    import urllib3
    from bs4 import BeautifulSoup

    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data)
    
    mydivs = soup.findAll("div", { "class" : "form-item" })
    return mydivs


mydivs = url_to_divs(url)

fields_list = []

for div in mydivs:
    fields = [x for x in div]
    fields_list.append(fields)
    print len(fields)  
            
headers = []
info = []
for i in fields_list:
    headers.append(i[1].text)
    info.append(i[2].lstrip().rstrip())
    
with open("metadata.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(headers)
    writer.writerow(info)
            