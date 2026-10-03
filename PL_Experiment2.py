import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

temp_low = [6.2, 15, 20, 25, 30, 40, 45, 50, 60, 70]
temp_high = [110, 130, 140, 180, 200, 240, 260, 280]
temp = [50, 60, 70]
# for i in range(10, 50, 5):
#     temp.append(i)
# for i in range(50, 160, 10):
#     temp.append(i)
# for i in range(160, 310, 20):
#     temp.append(i)
# fig, axes = plt.subplots(1, 2, figsize=(10, 8))
pos = ['right', 'left']
a = 0
for i in temp_low:
    file_path = r'Data 2/C665S3_TEMP_%d_1.csv' % i
    df = pd.read_csv(file_path)

    # mean = np.mean(df['Intensity'])
    # std = np.std(df['Intensity'])

    # x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    # y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std ** 2))

    # plt.plot(x, y, label='%d K' % i, linewidth=0.5)

    sb.lineplot(x='Wavelength(nm)', y='Intensity', data=df, label='%d K' % i)

    max_index = df['Intensity'].argmax()
    plt.text(df.loc[max_index, 'Wavelength(nm)'], df.loc[max_index, 'Intensity'], '%d K' % i, ha=pos[a], va='top')
    a = int(not a)
    # plt.xlabel('Intensity')
    # plt.ylabel('Probability Density')
    plt.grid(True)
    plt.legend()

# plt.title('Normal Distribution')
# plt.tight_layout()
plt.show()
