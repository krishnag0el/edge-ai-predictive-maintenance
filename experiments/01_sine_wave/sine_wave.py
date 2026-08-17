import numpy as np
import matplotlib.pyplot as plt
#time axis
t = np.linespace(0,1.1000)
#50 hz sine wave
x = np.sin(2*np.pi*50*t)

plt.plot(t, x)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("50 Hz Sine Wave")

# Save the figure
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")

plt.show()
