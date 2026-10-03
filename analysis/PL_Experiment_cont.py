import pandas as pd
import statistics as st
import seaborn as sb
from matplotlib import pyplot as plt
import os

temp = [6, 10, 20, 30, 40, 50, 72, 100, 125, 150, 175, 200, 225, 250, 275, 300]
file_num = list(range(1, 86))
for num in [67, 77]:
    file_num.remove(num)
x = 0
Temp_Wave = {'Temperature(K)': temp, 'Wavelength(nm)': []}

for i in temp:
    Max = []
    for j in range(0, 10):
        file_path = r'Data/Temp_%dK/C665S3_TEMP_%d_1.csv' % (i, file_num[x])
        if os.path.exists(file_path):
            x += 1
            df = pd.read_csv(file_path)
            max_index = df['Intensity'].argmax()
            wlngth_at_max_index = df.loc[max_index, 'Wavelength']
            Max.append(wlngth_at_max_index)

        else:
            break
    Temp_Wave['Wavelength(nm)'].append(round(st.mean(Max), 2))
Final_Data = pd.DataFrame(Temp_Wave)
print(Final_Data)
Final_Data = Final_Data.drop([1,2])


sb.lineplot(x='Temperature(K)', y='Wavelength(nm)', data=Final_Data)

plt.title('Peak Wavelength(nm) vs temp(avg. over Power)')
plt.grid(True)
plt.show()
