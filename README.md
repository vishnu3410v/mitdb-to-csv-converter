🫀MIT-BIH ECG Dataset to CSV Converter : 
  -This project converts raw MIT-BIH Arrhythmia Database .dat files into CSV format and visualizes ECG signals using Python. 
   Ideal for ECG signal preprocessing and machine learning applications in healthcare.


📁 Dataset
   We use the MIT-BIH Arrhythmia Database from PhysioNet, which contains ECG signals in .dat, .hea, and .atr formats.


✅ Features
   -Read ECG signals from MIT-BIH .dat files using wfdb

   -Extract signal and annotation data

   -Convert and save signals into CSV format

   -Plot ECG waveforms from CSV

   -Modular and customizable pipeline


⚙️ Installation

    -pip install wfdb pandas matplotlib numpy


📂 Project Structure
   graphql
   
   MITDB_to_CSV/
   │
   ├── convert_mitdb_to_csv.py     # Main script to convert .dat to .csv
   ├── plot_csv_ecg.py             # Script to visualize ECG from CSV
   ├── data/                       # Place MIT-BIH .dat, .atr, .hea files here
   ├── csv_output/                 # Converted CSV files stored here
   ├── example_plot.png            # Example ECG waveform plot
   └── README.md                   # This file


🚀 How to Use:

   1. Convert MITDB files to CSV:

           -python convert_mitdb_to_csv.py


   2. Plot the CSV as ECG waveform

          -python plot_csv_ecg.py


🧠 Example:     

  📌 Dependencies:
         -wfdb
         -numpy
         -pandas
         -matplotlib



📎 Notes:
     1. Ensure you download all three files per record: .dat, .hea, and .atr.
     2. or best results, use the sampling frequency and signal names directly from the header file via wfdb.

 
 
 🧑‍🔬 Future Improvements:
   
   -Signal filtering (e.g., baseline removal, noise reduction)

   -R-peak detection

   -HRV feature extraction

   -Export to EDF or HDF5 formats

  
  📜 License 

     -MIT License

    
