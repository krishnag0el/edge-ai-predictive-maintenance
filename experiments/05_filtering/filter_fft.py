import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt

fs=1000
duration=1
N=int(fs*duration)
t=np.arange(N)/fs
clean_signal=(np.sin(2*np.pi*50*t)+0.5*np.sin(2*np.pi*120*t))
noise=0.5*np.sin(2*np.pi*300*t)
noisy_signal=clean_signal+noise

cutoff=150
order=4
b,a=butter(order,cutoff/(fs/2),btype="low")
filtered_signal=filtfilt(b,a,noisy_signal)

def calculate_fft(signal):
  X=np.fft.fft(signal)
  magnitude=np.abs(X)/N
  magnitude=magnitude[:N//2]
  magnitude[1:]=2*magnitude[1:]
  frequencies=np.fft.fftfreq(N,1/fs)
  frequencies=frequencies[:N//2]
  return frequencies, magnitude

freq_noisy,fft_noisy=calculate_fft(noisy_signal)
freq_filtered,fft_filtered=calculate_fft(filtered_signal)

plt.plot(freq_noisy,fft_noisy,label="Before Filtering")
plt.plot(freq_filtered,fft_filtered,label="After Filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Before and After Filtering")
plt.xlim(0, 400)
plt.legend()
plt.grid()
plt.savefig("filter_fft_comparison.png",dpi=300,bbox_inches="tight")
plt.show()

