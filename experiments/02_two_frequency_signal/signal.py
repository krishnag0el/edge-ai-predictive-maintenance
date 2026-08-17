import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
duration = 1

# Time vector
t = np.linspace(0, duration, fs, endpoint=False)

# Frequency components
f1 = 50
f2 = 120

# Generate the composite signal
x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Plot the signal
plt.plot(t, x)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Two-Frequency Signal: 50 Hz + 120 Hz")
plt.grid()

# Save the plot
plt.savefig("two_frequency_signal.png", dpi=300, bbox_inches="tight")

plt.show()
