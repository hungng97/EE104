# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:22:38 2022

@author: thanh
"""

# Supraventricular tachycardia infant heart rate
#import packages
#import packages

import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 1000

data = hp.get_data('heart_beat_filter_Output_mono.csv')


plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

#run analysis
wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))