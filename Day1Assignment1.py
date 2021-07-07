import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x=np.arange(0,10)
y=3*x+10
plt.plot(x,y,'ro--')
plt.title('2d-Diagram',color='blue')
plt.xlabel('X-axis',color='blue')
plt.ylabel('Y-axis',color='blue')
plt.show()
