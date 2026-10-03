import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd

Data1 = pd.read_csv("LabData/08-09_g7_emission.csv", usecols=["Wavelength", "Intensity"])
Data2 = pd.read_csv("LabData/grp2610ex.ascii", usecols=["Wavelength", "Intensity"], delimiter='\t')

max1 = Data1['Intensity'].argmax()
max2 = Data2['Intensity'].argmax()

sb.lineplot(x='Wavelength', y='Intensity', data=Data2, label='Excitation')
sb.lineplot(x='Wavelength', y='Intensity', data=Data1, label='Emission')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')

plt.text(Data1.loc[max1, 'Wavelength'], Data1.loc[max1, 'Intensity'],
         '(%0.1f nm,%f)' % (Data1.loc[max1, 'Wavelength'], Data1.loc[max1, 'Intensity']), ha='right', va='bottom')
plt.text(575.5, 530.504494,
         '(%0.1f nm,%f)' % (575.5, 530.504494), ha='right', va='bottom')

plt.legend()

x_locator = ticker.MultipleLocator(base=50)
minor_locator = ticker.AutoMinorLocator(n=5)

plt.gca().xaxis.set_major_locator(x_locator)
plt.gca().xaxis.set_minor_locator(minor_locator)

plt.grid(True)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)

plt.title("Rhodamine B Emission and Excitation Spectrum")
plt.show()
