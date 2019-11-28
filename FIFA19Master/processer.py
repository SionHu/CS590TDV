import csv
import pandas as pd
import numpy as np

data = pd.read_csv("fifa19.csv")

overall = []
print(data)
for row in data:
    print(row)
print(overall)
