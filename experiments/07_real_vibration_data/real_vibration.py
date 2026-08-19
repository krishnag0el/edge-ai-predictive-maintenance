"""
EXP-07: Real Vibration Data Analysis

Dataset:
Case Western Reserve University (CWRU) Bearing Dataset

File analyzed:
98.mat

Condition:
Normal bearing, 1 HP load

Signal:
Drive End vibration (X098_DE_time)

Sampling frequency:
12 kHz
"""

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Load dataset
# ============================================================

data = loadmat("98.mat")

# Extract Drive End vibration signal
vibration = data["X098_DE_time"].flatten()


# ============================================================
# 2. Basic signal information
# ============================================================

print("Number of samples:", len(vibration))
print("Minimum:", vibration.min())
print("Maximum:", vibration.max())
print("Mean:", vibration.mean())
print("Standard deviation:", vibration.std())


# ============================================================
# 3. Plot raw vibration
# ============================================================

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


# ============================================================
# 4. FFT
# ============================================================

fs = 12000

N = len(window)

X = np.fft.fft(window)

magnitude = np.abs(X) / N

magnitude = magnitude[:N // 2]

magnitude[1:] = 2 * magnitude[1:]

frequencies = np.fft.fftfreq(N, 1 / fs)

frequencies = frequencies[:N // 2]


# ============================================================
# 5. Plot FFT spectrum
# ============================================================

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

plt.show()


# ============================================================
# 6. Low-frequency spectrum
# ============================================================

plt.figure(figsize=(12, 5))

plt.plot(frequencies, magnitude)

plt.xlim(0, 300)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "Low-Frequency Spectrum - Normal Bearing"
)

plt.grid()

plt.savefig(
    "low_frequency_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
