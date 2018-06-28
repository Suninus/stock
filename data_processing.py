#!/usr/bin/env python
import pandas as pd
import os 
from urllib import urlretrieve
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 


def load_data(download=True):
    # download data from : http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
    if download:
        data_path, _ = urlretrieve("http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data", "car.csv")
        print("Downloaded to car.csv")

    # use pandas to view the data structure
    col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    data = pd.read_csv("car.csv", names=col_names)
    return data


def convert2onehot(data):
    # covert data to onehot representation
    return pd.get_dummies(data, prefix=data.columns)


if __name__ == "__main__":
    data = load_data(download=True)
    new_data = convert2onehot(data)

    print(data.head())
    print "Num of data: %s" %len(data) # 1728
    # view data values
    for name in data.keys():
        print name, pd.unique(data[name])
    print new_data.head(2)
    new_data.to_csv("car_onehot.csv", index=False)
