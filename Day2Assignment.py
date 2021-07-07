import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import randn,randint,uniform,sample
d = pd.DataFrame(randn(10,4),columns=['a','b','c','d'])
print(d.head())
d.plot(kind='bar',title='Bar Chart',figsize=(10,10),grid=True,legend = True)
plt.show()
