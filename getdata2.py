#!/usr/bin/env python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd
import os 
from urllib import urlretrieve
import tushare as ts

if __name__=="__main__":
    with open('codelist.csv','rb') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            no_list.append((str(row[1])))
	#get da'pan zhi'shu hang'xing
	df=ts.get_hist_data('603993')
	filename='history2.csv'
	df.to_csv(filename,mode='a',header=None)
	
