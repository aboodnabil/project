import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
labels = 'frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = [0, 0.1, 0, 0]
fig1, ax1=plt.subplots()
ax1.pie(sizes,explode=explode, labels=labels,
autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

