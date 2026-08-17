import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
duration = 1
N = int(fs * duration)

# Time vector
t = np.arange(N) / fs

# Signal frequencies
f1 = 50
f2 = 120

# Clean signal
clean_signal = (
    np.sin(2 * np.pi * f1 * t)
    + 0.5 * np.sin(2 * np.pi * f2 * t)
)

# Add noise
noise = 0.5 * np.random.randn(N)

noisy_signal = clean_signal + noise

# FFT
X = np.fft.fft(noisy_signal)

# Magnitude
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
plt.title("FFT of Noisy Signal")
plt.grid()

plt.savefig(
    "noisy_fft.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
