import wfdb
import csv

record_name = '234'  # You can change this to another record like '101'

# Full path to the mitdb folder
data_path = 'mitdb'

# Read the signal and annotations
record = wfdb.rdrecord(f'{data_path}/{record_name}')
ann = wfdb.rdann(f'{data_path}/{record_name}', 'atr')

# Output file name (avoid conflicts)
output_file = f'{record_name}_converted.csv'

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['sample', 'time'] + record.sig_name + ['R_peak', 'R_type']
    writer.writerow(header)

    fs = record.fs
    sig = record.p_signal
    peeks = set(ann.sample)
    types = dict(zip(ann.sample, ann.symbol))

    for i, row in enumerate(sig):
        writer.writerow([
            i,
            i / fs,
            *row,
            1 if i in peeks else 0,
            types.get(i, '')
        ])
