# EXP-07: Real Vibration Data Analysis

## Objective

Analyze vibration measurements from a real rotating-machine
dataset instead of using mathematically generated signals.

This experiment introduces real-world vibration data into the
predictive-maintenance pipeline.

---

## Dataset

The dataset used is the Case Western Reserve University (CWRU)
Bearing Dataset.

Source:

Case Western Reserve University Bearing Data Center

The raw dataset is not stored in this repository.

---

## Dataset File

The file analyzed in this experiment is:

`98.mat`

This file represents a normal bearing condition under a 1 HP
motor load.

---

## Signal Used

The Drive End vibration signal was selected:

`X098_DE_time`

The signal contains approximately 483,903 samples.

The Fan End signal is also available:

`X098_FE_time`

but is not used in the first analysis.

---

## Sampling Frequency

The signal is analyzed using a sampling frequency of:

`12,000 Hz`

Therefore, the Nyquist frequency is:

`6,000 Hz`

---

## Analysis Pipeline

The experiment follows this pipeline:

Raw vibration data

↓

Signal inspection

↓

Time-domain visualization

↓

FFT

↓

Frequency-domain visualization

↓

Low-frequency analysis

---

## Results

### Raw Vibration

![Raw vibration](raw_vibration.png)

The real vibration signal is considerably more complex than the
synthetic signals used in earlier experiments.

---

### FFT Spectrum

![FFT spectrum](fft_spectrum.png)

The FFT reveals the frequency components present in the vibration
signal.

---

### Low-Frequency Spectrum

![Low-frequency spectrum](low_frequency_spectrum.png)

The low-frequency region is examined separately to make
rotational and other dominant components easier to identify.

---

## Important Observation

This experiment represents a normal bearing condition.

The frequency peaks observed in the spectrum should therefore
not automatically be interpreted as faults.

A faulty-bearing dataset will be analyzed separately and
compared with this baseline.

---

## Frequency Peak Analysis

The FFT spectrum was further analyzed using automated peak
detection.

Instead of manually identifying peaks from the plot, the
`scipy.signal.find_peaks` method was used to identify prominent
frequency components.

The analysis was limited to frequencies below 300 Hz for the
initial low-frequency investigation.

The approximate shaft speed for this operating condition is:

`1772 RPM`

which corresponds to an approximate rotational frequency of:

`29.53 Hz`

The detected peaks are treated as vibration features rather
than immediately being classified as bearing faults.

---

## Bearing Characteristic Frequencies

The Drive End bearing used in the CWRU dataset is a
6205-2RS JEM SKF deep-groove ball bearing.

The CWRU Bearing Data Center provides characteristic-frequency
multipliers for this bearing.

For the operating condition used in this experiment:

- Motor speed: 1772 RPM
- Rotational frequency: approximately 29.53 Hz
- FTF: approximately 11.76 Hz
- BPFO: approximately 105.84 Hz
- BSF: approximately 139.19 Hz
- BPFI: approximately 159.96 Hz

These theoretical frequencies provide reference points for
interpreting the measured vibration spectrum.

The presence of a peak near one of these frequencies does not,
by itself, establish that a bearing fault exists. Fault
diagnosis will be performed by comparing healthy and known
faulty datasets.

---

## Bearing Frequency Overlay

The measured FFT spectrum was compared with theoretical bearing
characteristic frequencies calculated from the approximate
operating speed.

![Bearing frequency overlay](bearing_frequency_overlay.png)

The theoretical frequencies are used as reference markers.
Their presence near measured spectral components does not by
itself indicate a bearing fault.

A reliable fault diagnosis requires comparison with known faulty
bearing data and additional signal-processing features.

---

## Engineering Interpretation

The spectrum contains multiple frequency components.

The presence of a frequency peak alone does not prove that a
bearing fault exists.

This experiment uses the normal-bearing signal as a baseline.
Fault diagnosis will require comparison against known faulty
bearing signals and, where appropriate, comparison with
theoretical bearing characteristic frequencies.

---

## Next Step

The next experiment will compare the normal bearing spectrum
against a known faulty-bearing signal.

The comparison will investigate:

- changes in dominant frequency components
- changes in vibration amplitude
- frequency-domain features
- bearing characteristic frequencies
- potential features for machine-learning models
