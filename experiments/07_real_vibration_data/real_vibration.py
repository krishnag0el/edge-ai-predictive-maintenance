from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

data = loadmat("98.mat")
vibration = data["X098_DE_time"].flatten()

print("Number of samples:", len(vibration))
print("Minimum:", vibration.min())
print("Maximum:", vibration.max())
print("Mean:", vibration.mean())
print("Standard deviation:", vibration.std())

window = vibration[:10000]

plt.figure(figsize=(12, 4))

plt.plot(window)

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Real Vibration Signal - Drive End")

plt.grid()

plt.savefig(
    "raw_vibration.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

fs = 12000
N = len(window)
X = np.fft.fft(window)
magnitude = np.abs(X) / N
magnitude = magnitude[:N // 2]
magnitude[1:] = 2 * magnitude[1:]
frequencies = np.fft.fftfreq(N, 1 / fs)
frequencies = frequencies[:N // 2]
plt.figure(figsize=(12, 5))
plt.plot(frequencies, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title(
    "FFT of Normal Bearing Vibration - Drive End"
)

plt.grid()

plt.savefig(
    "fft_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)
