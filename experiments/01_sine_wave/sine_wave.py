import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
duration = 1

# Time vector
t = np.linspace(0, duration, fs, endpoint=False)

# Generate a 50 Hz sine wave
f = 50
x = np.sin(2 * np.pi * f * t)

# Plot the signal
plt.plot(t, x)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("50 Hz Sine Wave")
plt.grid()

# Save the figure
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")

plt.show()
