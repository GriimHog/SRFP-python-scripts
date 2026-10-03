import os

import pandas as pd

temp = [6, 10, 20, 30, 40, 50, 72, 100, 125, 150, 175, 200, 225, 250, 275, 300]
file_num = list(range(1, 86))
for num in [67, 77]:
    file_num.remove(num)
x = 0
for i in temp:
    for j in range(0, 10):
        file_path = r'Data/Temp_%dK/C665S3_TEMP_%d_1.txt' % (i, file_num[x])
        new_file_path = r'Data/Temp_%dK/C665S3_TEMP_%d_1.csv' % (i, file_num[x])
        if os.path.exists(file_path):
            x += 1
            df = pd.read_csv(file_path, sep=",", header=None)
            df.to_csv(new_file_path, header=['Wavelength', 'Null', 'Intensity'], index=False)
            new_df = pd.read_csv(new_file_path)
            df_cln = new_df.groupby('Wavelength').mean().reset_index()
            df_cln.drop([0], axis=0, inplace=True)
            df_cln.drop(df_cln[df_cln['Wavelength'] > 635].index, inplace=True)
            df_cln.to_csv(new_file_path, index=False)

        else:
            break
