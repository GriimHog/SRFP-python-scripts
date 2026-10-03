import math
import statistics as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sb


def I0(P_av, w, R, t):
    return 4 * math.sqrt(math.log(2) / math.pi) * (P_av / (math.pi * (w ** 2) * R * t))


def model_t(z, B):
    P_aver = 0.2
    R = 80 * 10 ** -6
    t = 200.0 * 10 ** (-15)
    lmbd = 780 * 10 ** -9
    w = 35 * 10 ** -6
    L = 5 * 10 ** -3
    a0 = 0.001
    zr = math.pi * w ** 2 / lmbd

    x = z / zr
    Leff = (1 - math.exp(-a0 * L)) / a0
    q0 = B* Leff * I0(P_aver, w, R, t)

    def term(q, n, X):
        return ((-q) ** n) / (((n + 1) ** 1.5) * ((1 + X ** 2) ** n))

    tz = 0

    for i in range(200):
        tz = tz + term(q0, i, x)

    return tz
plt.plot()

data1 = pd.read_csv("TPA_f1foldamar_Final.csv", usecols=['Time', 'Transmittance'])

data1.Time = data1.Time.apply(lambda x: round(x, 2))
data1_cln = data1.groupby('Time').mean().reset_index()

data1_cln.Transmittance = data1_cln.Transmittance / data1_cln.Transmittance.max()
data1_cln.drop(data1_cln[data1_cln['Time'] > 5.9].index, inplace=True)
data1_cln.drop(data1_cln[data1_cln['Time'] < -5.9].index, inplace=True)
data1_cln = data1_cln.reset_index(drop=True)

data_reduced_time = data1_cln['Time'].iloc[::20]
data_reduced_time = data_reduced_time.reset_index(drop=True)
data_reduced_time = data_reduced_time+0.5

data_reduced_Transmittance = []
for i in range(0, len(data_reduced_time)):
    data_reduced_Transmittance.append(st.mean(data1_cln['Transmittance'].iloc[i * 20:(i + 1) * 20 - 1]))
data_final = pd.DataFrame(dict(x=data_reduced_time, y=data_reduced_Transmittance))
data_final = data_final.rename(columns={'x': 'Time', 'y': 'Transmittance'})

sb.lineplot(x='Time', y='Transmittance', data=data_final, marker='o', markersize=4)

cln_time = data_final.Time
cln_transmittance = data_final.Transmittance
popt, pcov = curve_fit(model_t, cln_time, cln_transmittance, p0=[10**-15])

# print(popt)
# print(pcov)
#
# plt.imshow(np.log(np.abs(pcov)))
# plt.colorbar()
# plt.show()

x_model = np.linspace(-10, 10, 1000)
y_model = model_t(x_model, 10**-2)

model_dict = dict(x=x_model, y=y_model)
model_data = pd.DataFrame(model_dict)
model_data = model_data.rename(columns={'x': 'Time', 'y': 'Transmittance'})
#
# model, plot = plt.subplots()
#
# sb.lineplot(x='Time', y='Transmittance', data=data1_cln)
sb.lineplot(x='Time', y='Transmittance', data=model_data)
plt.title('Z-scan Normalized Transmittance vs Time at 780 nm')
plt.show()
