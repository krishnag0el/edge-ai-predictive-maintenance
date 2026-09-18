import os
print("98.mat:", os.path.exists("98.mat"))
print("106.mat:", os.path.exists("106.mat"))
fault_data = loadmat("106.mat")
print(fault_data.keys())
for key in fault_data.keys():
  if key.startswith("X106"):
    print(key)
fault_vibration = fault_data["X106_DE_time"].flatten()
print("Signal loaded successfully.")
print("Number of samples:", len(fault_vibration))

print("Faulty Signal Statistics")
print("------------------")
print("Number of samples:", len(fault_vibration))
print("Minimum:", fault_vibration.min())
print("Maximum:", fault_vibration.max())
print("Mean:", fault_vibration.mean())
print("Standard deviation:", fault_vibration.std())

fs=12000
fault_window=fault_vibraton[:10000]
fault_time = np.arange(len(fault_window)) / fs

plt.figure(figsize=(12, 4))

plt.plot(fault_time, fault_window)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.title(
    "Faulty Bearing Vibration - Drive End"
)

plt.grid()
plt.tight_layout()

plt.savefig(
    "fault_raw_vibration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
