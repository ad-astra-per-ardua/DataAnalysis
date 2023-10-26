import pandas as pd
import numpy as np
import seaborn as sns

d = sns.load_dataset('penguins')

print(d.describe(include=[np.number]))
