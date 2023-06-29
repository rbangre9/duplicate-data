import duplicates
import numpy as np 
import pandas as pd 

data = pd.read_csv('.\example-data\pme_full_unlabelled.csv')
data2 = pd.read_csv('./example-data/smalldata1.csv')

print(duplicates.find_duplicate_rows(data2))
