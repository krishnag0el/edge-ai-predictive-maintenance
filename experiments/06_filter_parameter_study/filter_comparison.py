import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt
fs=1000
duration=1
N=int(fs*duration)
t=np.arange(N)/fs
signal=(np.sin(2*np.pi*50*t)+0.5*np.sin(2*np.pi*120*t)+0.5*np.sin(2*np.pi*300*t))
cutoffs=[80,150,200]
plt.figure()
for cutoff in cutoffs:
  b,a=butter(4,cutoff/(fs/2),btype="low")

filtered=filtfilt(b,a,signal)
plt.plot(t,filtered,label=f"{cutoff} Hz cutoff")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Effect of Low-Pass Filter Cutoff Frequency")
plt.xlim(0, 0.2)
plt.legend()
plt.grid()
plt.savefig("cutoff_comparison.png",dpi=300,bbox_inches="tight")
plt.show()
