import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# temp_low = []
# temp_high = []
# fig, axes = plt.subplots(1, 2, figsize=(10, 8))
temp = [6.2]
for i in range(10, 50, 5):
    temp.append(i)
for i in range(50, 160, 10):
    temp.append(i)
for i in range(160, 310, 20):
    temp.append(i)
d = {}
for i in range(1, len(temp) + 1):
    file_path = r'Data 2/C665S3_TEMP1_%d_1.csv' % i
    df = pd.read_csv(file_path)

    mean = np.mean(df['Intensity'])
    std = np.std(df['Intensity'])

    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std ** 2))

    d['x_%d' % temp[i - 1]] = x
    d['y_%d' % temp[i - 1]] = y

Normal_Data = pd.DataFrame(d)
Normal_Data.to_csv(r'NormalData', index=False)
