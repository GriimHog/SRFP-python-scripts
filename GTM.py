import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\kuber\\Downloads\\SphereData.csv")
data = pd.DataFrame(data)
for i in range(data.shape[0]):
    for j in data.columns:
        if np.isnan(data.loc[i,j]):
            data.loc[i,j] = 0
c_ra = 266.41683333
c_dec = -29.00780556
r_s = 300
# width = np.degrees(np.arctan(r_s / 100))
width = np.degrees(np.arctan(r_s / 8000))
width = width / 10
for i in range(data.shape[0]):
    c_ra = data.iloc[i]['ra']
    c_dec = data.iloc[i]['dec']
    a1 = round(c_ra + width,3)
    a2 = round(c_ra - width,3)
    b1 = round(c_dec + width,3)
    b2 = round(c_dec - width,3)
    counter = 0
    counter_list = []
    for i in range(data.shape[0]):
        if (a2 < data.iloc[i]['ra'] and a1 > data.iloc[i]['ra']) and (b2 < data.iloc[i]['dec'] and b1 > data.iloc[i]['dec']):
                counter = counter + 1
    #data1.loc[i,'count_cir'] = counter
    counter_list.append(counter)
data['count_cent'] = counter_list
print(data)
