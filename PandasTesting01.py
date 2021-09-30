#Beginner Pandas

import numpy as np
import pandas as pd

#creating a series
seriestime = pd.Series([1,3,5, np.nan, 6, 8])
print(seriestime)

dates = pd.date_range("20210101", periods=6)
print(dates)