import pandas as pd
from torch.backends.quantized import engine

redW = pd.read_csv('./w_q/winequality-red.csv', sep=';', header=0, engine='python')
whiteW = pd.read_csv('./w_q/winequality-white.csv', sep=';', header=0, engine='python')

redW.to_csv('./w_q/winequality-red_4lecture.csv', index=False)
whiteW.to_csv('./w_q/winequality-white_4lecture.csv', index=False)

redW.head()