import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd

Data = pd.read_csv("LabData/ItemData.csv", usecols=["θ/2θ", "Intensity"])

sb.lineplot(x='θ/2θ', y='Intensity', data=Data, label='XRD Scattering Amplitudes at Various angles')

plt.xlabel('θ/2θ')
plt.ylabel('Intensity')

plt.legend()

plt.grid(True)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)

plt.show()
