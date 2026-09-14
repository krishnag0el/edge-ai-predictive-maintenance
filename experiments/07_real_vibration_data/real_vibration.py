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

# Detect dominant frequency peaks
from scipy.signal import find_peaks

peaks, properties = find_peaks(
    magnitude,
    prominence=0.001
)

peak_frequencies = frequencies[peaks]
peak_amplitudes = magnitude[peaks]

# Keep frequencies below 300 Hz
mask = peak_frequencies <= 300

peak_frequencies = peak_frequencies[mask]
peak_amplitudes = peak_amplitudes[mask]

# Sort by amplitude
order = np.argsort(peak_amplitudes)[::-1]

peak_frequencies = peak_frequencies[order]
peak_amplitudes = peak_amplitudes[order]

print("\nTop frequency peaks below 300 Hz:")

for i in range(min(15, len(peak_frequencies))):

    print(
        f"{i + 1:2d}. "
        f"{peak_frequencies[i]:8.2f} Hz  "
        f"Amplitude = {peak_amplitudes[i]:.6f}"
    )


# 8. Calculate rotational frequency
rpm = 1772

rotation_frequency = rpm / 60

print(
    f"\nApproximate rotational frequency: "
    f"{rotation_frequency:.2f} Hz"
)
