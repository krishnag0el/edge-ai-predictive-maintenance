import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.io import loadmat
from scipy.signal import find_peaks
data = loadmat("98.mat")

print("Variables available in the dataset:")
print(data.keys())

vibration = data["X098_DE_time"].flatten()

print("Signal loaded successfully.")
print("Number of samples:", len(vibration))

print("Signal Statistics")
print("------------------")

print("Number of samples:", len(vibration))
print("Minimum:", vibration.min())
print("Maximum:", vibration.max())
print("Mean:", vibration.mean())
print("Standard deviation:", vibration.std())

print("Signal Statistics")
print("------------------")

print("Number of samples:", len(vibration))
print("Minimum:", vibration.min())
print("Maximum:", vibration.max())
print("Mean:", vibration.mean())
print("Standard deviation:", vibration.std())

fs = 12000
duration = len(vibration) / fs

print("Sampling frequency:", fs, "Hz")
print("Signal duration:", duration, "seconds")

window = vibration[:10000]

plt.figure(figsize=(12, 4))

plt.plot(window)

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Real Vibration Signal - Drive End")

plt.grid()
plt.tight_layout()

plt.savefig(
    "raw_vibration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

time = np.arange(len(window)) / fs

plt.figure(figsize=(12, 4))

plt.plot(time, window)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Real Vibration Signal - Time Domain")

plt.grid()
plt.tight_layout()

plt.show()

N = len(window)

X = np.fft.fft(window)

magnitude = np.abs(X) / N

magnitude = magnitude[:N // 2]

magnitude[1:] = 2 * magnitude[1:]

frequencies = np.fft.fftfreq(
    N,
    1 / fs
)

frequencies = frequencies[:N // 2]

print("FFT calculated successfully.")
print("FFT points:", len(frequencies))
print("Maximum frequency:", frequencies[-1], "Hz")

plt.figure(figsize=(12, 5))

plt.plot(
    frequencies,
    magnitude
)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "FFT of Normal Bearing Vibration - Drive End"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "fft_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.figure(figsize=(12, 5))

plt.plot(
    frequencies,
    magnitude
)

plt.xlim(0, 300)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "Low-Frequency Spectrum - Normal Bearing"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "low_frequency_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

peaks, properties = find_peaks(
    magnitude,
    prominence=0.001
)

peak_frequencies = frequencies[peaks]
peak_amplitudes = magnitude[peaks]

print("Total detected peaks:", len(peak_frequencies))

mask = peak_frequencies <= 300

peak_frequencies = peak_frequencies[mask]
peak_amplitudes = peak_amplitudes[mask]

print(
    "Detected peaks below 300 Hz:",
    len(peak_frequencies)
)

num_peaks = min(
    15,
    len(peak_frequencies)
)

peak_table = pd.DataFrame({
    "Rank": range(1, num_peaks + 1),
    "Frequency_Hz": peak_frequencies[:num_peaks],
    "Amplitude": peak_amplitudes[:num_peaks]
})

display(peak_table)

peak_table.to_csv(
    "peak_analysis.csv",
    index=False
)

print("peak_analysis.csv created successfully.")

rpm = 1772

fr = rpm / 60

print(
    f"Rotational Frequency (1X): {fr:.2f} Hz"
)

FTF_multiplier = 0.39828
BPFO_multiplier = 3.5848
BPFI_multiplier = 5.4152
BSF_multiplier = 4.7135

FTF = FTF_multiplier * fr
BPFO = BPFO_multiplier * fr
BPFI = BPFI_multiplier * fr
BSF = BSF_multiplier * fr

print(f"Rotational Frequency (1X): {fr:.2f} Hz")
print(f"FTF:  {FTF:.2f} Hz")
print(f"BPFO: {BPFO:.2f} Hz")
print(f"BSF:  {BSF:.2f} Hz")
print(f"BPFI: {BPFI:.2f} Hz")

bearing_frequencies = pd.DataFrame({
    "Component": [
        "Rotational Frequency (1X)",
        "FTF",
        "BPFO",
        "BSF",
        "BPFI"
    ],
    "Frequency_Hz": [
        fr,
        FTF,
        BPFO,
        BSF,
        BPFI
    ]
})

display(bearing_frequencies)

bearing_frequencies.to_csv(
    "bearing_characteristic_frequencies.csv",
    index=False
)

print(
    "bearing_characteristic_frequencies.csv created."
)

plt.figure(figsize=(12, 5))

plt.plot(
    frequencies,
    magnitude,
    label="Measured FFT"
)

plt.xlim(0, 300)

plt.axvline(
    fr,
    linestyle="--",
    label=f"1X = {fr:.2f} Hz"
)

plt.axvline(
    FTF,
    linestyle="--",
    label=f"FTF = {FTF:.2f} Hz"
)

plt.axvline(
    BPFO,
    linestyle="--",
    label=f"BPFO = {BPFO:.2f} Hz"
)

plt.axvline(
    BSF,
    linestyle="--",
    label=f"BSF = {BSF:.2f} Hz"
)

plt.axvline(
    BPFI,
    linestyle="--",
    label=f"BPFI = {BPFI:.2f} Hz"
)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.title(
    "Normal Bearing FFT with Theoretical Bearing Frequencies"
)

plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()

plt.savefig(
    "bearing_frequency_overlay.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

summary = pd.DataFrame({
    "Parameter": [
        "Dataset File",
        "Signal",
        "Condition",
        "Sampling Frequency",
        "Number of Samples",
        "Motor Speed",
        "Rotational Frequency",
        "FTF",
        "BPFO",
        "BSF",
        "BPFI"
    ],
    "Value": [
        "98.mat",
        "X098_DE_time",
        "Normal, 1 HP",
        "12000 Hz",
        len(vibration),
        "1772 RPM",
        f"{fr:.2f} Hz",
        f"{FTF:.2f} Hz",
        f"{BPFO:.2f} Hz",
        f"{BSF:.2f} Hz",
        f"{BPFI:.2f} Hz"
    ]
})

display(summary)

import os

files = [
    "raw_vibration.png",
    "fft_spectrum.png",
    "low_frequency_spectrum.png",
    "peak_analysis.csv",
    "bearing_characteristic_frequencies.csv",
    "bearing_frequency_overlay.png"
]

print("Experiment output files:")
print("------------------------")

for file in files:
    if os.path.exists(file):
        print("✓", file)
    else:
        print("✗", file, "NOT FOUND")
        
