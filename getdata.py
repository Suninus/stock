#!/usr/bin/env python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd
import os 
from urllib import urlretrieve
import tushare as ts
import csv

if __name__=="__main__":
    no_list=[]
    with open('history.csv','rb') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            no_list.append((str(row[1])))
    
    with open('codelist.csv','wb') as myfile:
        myWriter=csv.writer(myfile)
        myWriter.writerows([no_list])
	
