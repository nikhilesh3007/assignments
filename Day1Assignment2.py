import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


x=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
y=[160,150,140,145,175,165,180]
plt.plot(x,y,'ro--')
plt.title('SALES',color='blue')
plt.xlabel('DAYS OF WEEK',color='blue')
plt.ylabel('SALES',color='blue')
plt.show()
