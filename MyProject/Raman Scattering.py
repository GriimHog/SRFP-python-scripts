import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd

Data1 = pd.read_csv("Group7 Raman/Group7_Ethanol.csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data2 = pd.read_csv("Group7 Raman/Group7_CCl4.csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data3 = pd.read_csv("Group7 Raman/Group7_Benzene.csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data4 = pd.read_csv("Group7 Raman/Group7_Glycerol.csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data5 = pd.read_csv("Group7 Raman/Group7_Propanal.csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data6 = pd.read_csv("Group7 Raman/Group7_Mix (Ethanol and CCl4).csv", usecols=["Wavenumber (cm-1)", "Intensity"])
Data7 = pd.read_csv("Group7 Raman/Group7_Mix (Ethanol and Glycerol).csv", usecols=["Wavenumber (cm-1)", "Intensity"])




# max1 = Data1['Intensity'].argmax()
# max2 = Data2['Intensity'].argmax()

# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data1, label='Ethanol')
# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data2, label='CCl_4')
# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data3, label='Benzene')
# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data4, label='Glycerol')
sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data5, label='Propanol')
# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data6, label='Ethanol and CCL4 Mix 1:1')
# sb.lineplot(x='Wavenumber (cm-1)', y='Intensity', data=Data7, label='Ethanol and Glycerol Mix 1:1')




plt.xlabel('Wavenumber (cm-1)')
plt.ylabel('Intensity')


# plt.text(Data1.loc[max1, 'Wavenumber (cm-1)'], Data1.loc[max1, 'Intensity'],
#          '(%0.1f nm,%f)' % (Data1.loc[max1, 'Wavenumber (cm-1)'], Data1.loc[max1, 'Intensity']), ha='right', va='bottom')
# plt.text(575.5, 530.504494,
#          '(%0.1f nm,%f)' % (575.5, 530.504494), ha='right', va='bottom')

plt.legend()

# x_locator = ticker.MultipleLocator(base=50)
# minor_locator = ticker.AutoMinorLocator(n=5)

# plt.gca().xaxis.set_major_locator(x_locator)
# plt.gca().xaxis.set_minor_locator(minor_locator)

plt.grid(True)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)

# plt.title()
plt.show()
