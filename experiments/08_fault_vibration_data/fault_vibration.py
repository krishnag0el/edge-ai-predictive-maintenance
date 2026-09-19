import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
print("98.mat:", os.path.exists("98.mat"))
print("106.mat:", os.path.exists("106.mat"))
fault_data = loadmat("106.mat")
print(fault_data.keys())
for key in fault_data.keys():
  if key.startswith("X106"):
    print(key)
fault_vibration = fault_data["X106_DE_time"].flatten()
print("Signal loaded successfully.")
print("Number of samples:", len(fault_vibration))

print("Faulty Signal Statistics")
print("------------------")
print("Number of samples:", len(fault_vibration))
print("Minimum:", fault_vibration.min())
print("Maximum:", fault_vibration.max())
print("Mean:", fault_vibration.mean())
print("Standard deviation:", fault_vibration.std())

fs=12000
fault_window=fault_vibraton[:10000]
fault_time = np.arange(len(fault_window)) / fs

plt.figure(figsize=(12, 4))

plt.plot(fault_time, fault_window)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.title(
    "Faulty Bearing Vibration - Drive End"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "fault_raw_vibration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

N = len(fault_window)
X_fault = np.fft.fft(fault_window)
fault_magnitude = np.abs(X_fault) / N
fault_magnitude = fault_magnitude[:N // 2]
fault_magnitude[1:] = 2 * fault_magnitude[1:]
fault_frequencies = np.fft.fftfreq(N,1 / fs)
fault_frequencies = fault_frequencies[:N // 2]

print("Fault FFT calculated successfully.")
print("Maximum frequency:", fault_frequencies[-1], "Hz")


plt.figure(figsize=(12, 5))

plt.plot(
    fault_frequencies,
    fault_magnitude
)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "FFT of Faulty Bearing Vibration - Drive End"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "fault_fft_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.figure(figsize=(12, 5))

plt.plot(
    fault_frequencies,
    fault_magnitude
)
plt.xlim(0, 300)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "FFT of Faulty Bearing Vibration - Drive End"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "fault_low_frequency_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

normal_data = loadmat("98.mat")
normal_vibration = normal_data["X098_DE_time"].flatten()
normal_window = normal_vibration[:10000]
N_normal = len(normal_window)
X_normal = np.fft.fft(normal_window)
normal_magnitude = np.abs(X_normal) / N_normal
normal_magnitude = normal_magnitude[:N_normal // 2]
normal_magnitude[1:] = 2 * normal_magnitude[1:]
normal_frequencies = np.fft.fftfreq(N_normal,1 / fs)
normal_frequencies = normal_frequencies[:N_normal // 2]

plt.figure(figsize=(12, 5))
plt.plot(
    normal_frequencies,
    normal_magnitude,
    label="Normal Bearing"
)
plt.plot(
    fault_frequencies,
    fault_magnitude,
    label="Inner-Race Fault"
)
plt.xlim(0, 300)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Normal vs Faulty Bearing FFT Comparison")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(
    "normal_vs_fault_fft.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
