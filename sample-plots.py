#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

pressureTargets = pd.read_csv("PressureTargets.csv", sep=",")
# Get the unique delta cases to generate plots for later on.
allDeltaCases = pressureTargets['DeltaCase'].unique()

#%%

# Look at pressures that are above a certain range
case2 = pressureTargets.loc[pressureTargets['DeltaPressure'] > 1000]
case2.head()
case2.to_csv('high_pressures.csv', sep=',')

#%%
# Generate some plots of the different delta cases
plt.figure(figsize=(6,8))

def plotChart(deltaCase, allPressureTargets):
  fig, ax = plt.subplots()
  data = allPressureTargets.loc[allPressureTargets['DeltaCase'] == deltaCase]
  wellData = data['Well'].values
  pressueData = data['DeltaPressure'].values
  plot = ax.bar(wellData, pressueData, color='b', label=deltaCase)
  ax.set_xlabel('Well Name')
  ax.set_ylabel('Pressue')
  ax.set_title(deltaCase)
  ax.legend()

def plotScatter(deltaCase, allPressureTargets):
  data = allPressureTargets.loc[allPressureTargets['DeltaCase'] == deltaCase]
  x = data['Well'].values
  y = data['DeltaPressure'].values
  # area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

  plt.scatter(x, y, s=1, c=1, alpha=0.5)
  plt.show()

for deltaCase in allDeltaCases:
  plotChart(deltaCase, pressureTargets)




