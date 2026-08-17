import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
duration = 1

# Number of samples
N = int(fs * duration)

# Time vector
t = np.arange(N) / fs

# Frequencies
f1 = 50
f2 = 120

# Generate signal
x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Perform FFT
X = np.fft.fft(x)

# Two-sided magnitude spectrum
magnitude = np.abs(X) / N

# Single-sided spectrum
magnitude = magnitude[:N // 2]
magnitude[1:] = 2 * magnitude[1:]

# Frequency axis
frequencies = np.fft.fftfreq(N, 1 / fs)
frequencies = frequencies[:N // 2]

# Plot
plt.plot(frequencies, magnitude)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Single-Sided FFT Spectrum")
plt.grid()

plt.savefig("fft_spectrum_normalized.png",
            dpi=300,
            bbox_inches="tight")

plt.show()

