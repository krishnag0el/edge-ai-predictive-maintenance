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

# Calculate magnitude
magnitude = np.abs(X)

# Frequency axis
frequencies = np.fft.fftfreq(N, 1 / fs)

# Plot only positive frequencies
positive = frequencies >= 0

plt.plot(frequencies[positive], magnitude[positive])

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of Two-Frequency Signal")
plt.grid()

plt.savefig("fft_spectrum.png", dpi=300, bbox_inches="tight")

plt.show()
