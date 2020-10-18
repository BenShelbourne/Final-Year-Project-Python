import pandas as pd
import numpy as np
import scipy as sp
import csv

AEON = pd.read_csv("AEON 1998-2005.csv", delimiter=',')
AMAZON = pd.read_csv("Amazon 1998-2005.csv", delimiter=',')
Astra = pd.read_csv("Astra Zeneca 1998-2005.csv", delimiter=',')
Boeing = pd.read_csv("Boeing 1998-2005.csv", delimiter=',', header = 0)
Canon = pd.read_csv("Canon 1998-2005.csv", delimiter=',')
Comcast = pd.read_csv("Comcast 1998-2005.csv", delimiter=',')
Dior = pd.read_csv("Dior 1998-2005.csv", delimiter=',')
Disney = pd.read_csv("Disney 1998-2005.csv", delimiter=',')
GD = pd.read_csv("General Dynamics 1998-2005.csv", delimiter=',')
Halliburton = pd.read_csv("Halliburton 1998-2005.csv", delimiter=',')
Lockheed = pd.read_csv("Lockheed Martin 1998-2005.csv", delimiter=',', header = 0)
Mcdonalds = pd.read_csv("Mcdonalds 1998-2005.csv", delimiter=',')
Nokia = pd.read_csv("Nokia 1998-2005.csv", delimiter=',')
Panasonic = pd.read_csv("Panasonic 1998-2005.csv", delimiter=',')
Pepsico = pd.read_csv("Pepsico 1998-2005.csv", delimiter=',')
Rothschild = pd.read_csv("Rothschild 1998-2005.csv", delimiter=',')
Softbank = pd.read_csv("Softbank 1998-2005.csv", delimiter=',')
Tata = pd.read_csv("Tata Chemicals 1998-2005.csv", delimiter=',')
Texas = pd.read_csv("Texas Instruments 1998-2005.csv", delimiter=',')
WestJapan = pd.read_csv("West Japan Railway 1998-2005.csv", delimiter=',')


values = {"X":[Lockheed],

          "Y":[Boeing]
};




dataFrame       = pd.DataFrame(data=values);

print("DataFrame:");

print(dataFrame);

 

corrrelation    = dataFrame.corr(method="pearson");

print("Pearson correlation coefficient:");

print(corrrelation)