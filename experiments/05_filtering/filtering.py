import numpy as np
import matplotlib.pyplot as plt
import spicy.signal
import butter,filtfilt
fs=1000
duration=1
N=int(duration*fs)
t=np.arrange(N)/fs
signal=np.sine(2*np.pi*50*t)+0.5*np.sine(2*np.pi*120*t)
noise=0.5*np.sine(2*np.pi*300*t)
noisy_signal=signal+noise

cutoff=150
order=4
b,a=butter(order,cutoff/(fs/2),btype="low")
filtered_signal=filtfilt(b,a,noisy_signal)

plt.figure
plt.plot(t,noisy_signal,label="Noisy Signal")
plt.plot(t,filtered_signal,label="Filtered Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Low-Pass Filtering")
plt.legend()
plt.grid()
plt.savefig("filtered_signal.png",dpi=300,bbox_index=tight)
plt.show()
