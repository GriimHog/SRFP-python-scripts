import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import os

temp = [6, 10, 20, 30, 40, 50, 72, 100, 125, 150, 175, 200, 225, 250, 275, 300]
file_num = list(range(1, 86))
for num in [67, 77]:
    file_num.remove(num)
x = 0
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for i in temp:
    plt.figure(i)
    for j in range(0, 10):
        file_path = r'Data/Temp_%dK/C665S3_TEMP_%d_1.csv' % (i, file_num[x])
        if os.path.exists(file_path):
            x += 1
            df = pd.read_csv(file_path)

            sb.lineplot(x='Wavelength', y='Intensity', data=df, label=f'{(j+2)*2.5} mW')
        else:
            break
    plt.title(f'{i} K')
    plt.legend()
    plt.grid(True)
    plt.show()
