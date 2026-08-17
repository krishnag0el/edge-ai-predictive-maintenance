import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# -----------------------------
# Sampling parameters
# -----------------------------
fs = 1000
duration = 1
N = int(fs * duration)

# Time vector
t = np.arange(N) / fs

# -----------------------------
# Create useful signal
# -----------------------------
signal = (
    np.sin(2 * np.pi * 50 * t)
    + 0.5 * np.sin(2 * np.pi * 120 * t)
)

# -----------------------------
# Add high-frequency noise
# -----------------------------
noise = 0.5 * np.sin(2 * np.pi * 300 * t)

noisy_signal = signal + noise

# -----------------------------
# Design low-pass filter
# -----------------------------
cutoff = 150
order = 4

b, a = butter(
    order,
    cutoff / (fs / 2),
    btype="low"
)

# Apply filter
filtered_signal = filtfilt(
    b,
    a,
    noisy_signal
)

# -----------------------------
# Plot signals
# -----------------------------
plt.figure()

plt.plot(t, noisy_signal, label="Noisy Signal")
plt.plot(t, filtered_signal, label="Filtered Signal")

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Low-Pass Filtering")
plt.legend()
plt.grid()

plt.savefig(
    "filtered_signal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
