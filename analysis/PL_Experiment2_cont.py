import pandas as pd
import statistics as st
import seaborn as sb
from matplotlib import pyplot as plt

file_num = list(range(1, 33))
temp = [6.2]
for i in range(10, 50, 5):
    temp.append(i)
for i in range(50, 160, 10):
    temp.append(i)
for i in range(160, 310, 20):
    temp.append(i)
for num in [17, 26, 20, 21]:
    file_num.remove(num)
Temp_Wave = {'Temperature(K)': temp, 'Wavelength(nm)': []}

for i in file_num:
    if i == 16 or i == 25:
        Max = []
        for j in [0, 1]:
            file_path = fr'Data 2/C665S3_TEMP1_{i + j}_1.csv'
            df = pd.read_csv(file_path)
            max_index = df['Intensity'].argmax()
            wlngth_at_max_index = df.loc[max_index, 'Wavelength']
            Max.append(wlngth_at_max_index)
        Temp_Wave['Wavelength(nm)'].append(round(st.mean(Max), 2))
    else:
        file_path = fr'Data 2/C665S3_TEMP1_{i}_1.csv'
        df = pd.read_csv(file_path)
        max_index = df['Intensity'].argmax()
        wlngth_at_max_index = df.loc[max_index, 'Wavelength']
        Temp_Wave['Wavelength(nm)'].append(wlngth_at_max_index)
Final_Data = pd.DataFrame(Temp_Wave)
print(Final_Data)
Final_Data = Final_Data.drop([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 22, 23, 25])

sb.lineplot(x='Temperature(K)', y='Wavelength(nm)', data=Final_Data)

plt.grid(True)
plt.title('Peak Wavelength(nm) at various Temperatures')
plt.show()
