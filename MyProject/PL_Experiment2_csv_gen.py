import pandas as pd

temp = [6.2]
for i in range(10, 50, 5):
    temp.append(i)
for i in range(50, 160, 10):
    temp.append(i)
for i in range(160, 310, 20):
    temp.append(i)
for i in range(1, len(temp)+1):
    file_path = r'Data 2/C665S3_TEMP1_%d_1.txt' % i
    new_file_path = r'Data 2/C665S3_TEMP_%d_1.csv' % temp[i-1]
    df = pd.read_csv(file_path, sep=",", header=None)
    df.to_csv(new_file_path, header=['Wavelength(nm)', 'Null', 'Intensity'], index=False)
    new_df = pd.read_csv(new_file_path)
    df_cln = new_df.groupby('Wavelength(nm)').mean().reset_index()
    df_cln.drop([0], axis=0, inplace=True)
    df_cln.drop(df_cln[df_cln['Wavelength(nm)'] > 670].index, inplace=True)
    df_cln.to_csv(new_file_path, index=False)
