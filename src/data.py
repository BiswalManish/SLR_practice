#Creating a pandas dataframe from the .csv file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import sys
sys.path.insert(0, '/Users/manish/Documents/Projects/data_science/SLR_practice/src')

import warnings
warnings.filterwarnings('ignore')

path = '/Users/manish/Documents/Projects/data_science/SLR_practice/data/raw data/advertising.csv'

adv = pd.read_csv(path)

