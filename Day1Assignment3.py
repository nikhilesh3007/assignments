import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
sales_1=[160,150,140,145,175,165,180]
sales_2=[70,90,160,150,140,145,175]
plt.figure(figsize=(6,5), dpi=150)
plt.plot(days,sales_1,'ro--')
plt.plot(days,sales_2,'go--')
plt.title('SALES TRENDS',color='blue')
plt.xlabel('DAYS OF WEEK',color='blue')
plt.ylabel('SALES',color='blue')
plt.show()
