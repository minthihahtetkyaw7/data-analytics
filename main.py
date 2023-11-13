import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport


df = pd.read_csv("cardio_data_processed.csv")
df.head()