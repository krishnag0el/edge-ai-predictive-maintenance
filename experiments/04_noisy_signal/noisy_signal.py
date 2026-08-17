import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
duration = 1

# Number of samples
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

# Generate Gaussian noise
noise = 0.5 * np.random.randn(N)

# Add noise
noisy_signal = clean_signal + noise

# Plot noisy signal
plt.plot(t, noisy_signal)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Noisy Two-Frequency Signal")
plt.grid()

plt.savefig(
    "noisy_signal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
