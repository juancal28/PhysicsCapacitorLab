import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

contourData = pd.read_csv('voltage.csv')

plt.figure(figsize=(21,26))
cs = plt.contourf(contourData, linewidths=1.5, levels= 30)
a = plt.colorbar(label='Voltage', )
plt.show()