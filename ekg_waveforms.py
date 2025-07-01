import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (replace with your actual filename)
csv_file = "234_converted.csv"  # e.g. '800.csv' if that's your file
df = pd.read_csv(csv_file)

# Show column names so you can verify which signal to plot
print("Available columns:", df.columns)

# Replace with the actual ECG signal column name (e.g., 'MLII', 'V1', etc.)
signal_column = 'MLII'      # Change to 'V1' or other if needed
time_column = 'time'
rpeak_column = 'R_peak'

# Plot the ECG signal
plt.figure(figsize=(14, 5))
plt.plot(df[time_column], df[signal_column], label=signal_column, color='blue')

# Overlay R-peaks if the column exists
if rpeak_column in df.columns:
    r_peaks = df[df[rpeak_column] == 1]
    plt.plot(r_peaks[time_column], r_peaks[signal_column], 'ro', label='R-peaks')

# Label the plot
plt.title(f"EKG Waveform from {csv_file}")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
