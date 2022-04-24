# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

freq1=3 #1Hz
time_step = 0.02
period1 = 1/freq1
time_vec = np.arange(0, 20, time_step)

sig1 = (np.sin(2 * np.pi / period1 * time_vec))
plt.figure(figsize=(60, 10))
plt.plot(time_vec, sig1, label='Low Frequency')

freq2=12 #10Hz
period2 = 1/freq2
noise_amplitude = 0.5
sig2 = noise_amplitude*(np.sin(2 * np.pi / period2 * time_vec))
plt.figure(figsize=(60, 10))
plt.plot(time_vec, sig2, label='High Frequency')

freq3=15 #10Hz
period3 = 1/freq3
noise_amplitude3 = 0.5
sig3 = noise_amplitude3*(np.sin(2 * np.pi / period3 * time_vec))
plt.figure(figsize=(60, 10))
plt.plot(time_vec, sig3, label='High Frequency')

############################################################
# Generate the signal
############################################################
sig = sig1 + sig2 + sig3
plt.figure(figsize=(60,10))
plt.plot(time_vec, sig, label='Low & High Frequency')

############################################################
# Compute and plot the power
############################################################
# The FFT of the signal
sig_fft = fftpack.fft(sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Plot the FFT power
plt.figure(figsize=(30, 20))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('power')


# Find the peak frequency: we can focus on only the positive frequencies
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]
peak_freq


############################################################
# Remove all the high frequencies
############################################################
#
# We now remove all the high frequencies and transform back from
# frequencies to signal.

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

plt.figure(figsize=(60,10))
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.legend(loc='best')


############################################################
# Double check: Re-Compute and plot the power
############################################################
#sig = filtered_sig
# The FFT of the signal
sig_fft1 = fftpack.fft(filtered_sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft1)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(filtered_sig.size, d=time_step)

# Plot the FFT power
plt.figure(figsize=(30, 20))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')
# It should look very clean now

