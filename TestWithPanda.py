import os
import time
import csv
import socket
import json
import math
import pandas as pd


def watch_for_new_csv_files(directory):
    """
    Watches for new CSV files in the specified directory and loads the contents
    into a dictionary with three keys corresponding to the three columns.
    """
    file_paths = set()
    while True:
        # Get a list of all CSV files in the directory
        new_file_paths = set([os.path.join(directory, f)
                             for f in os.listdir(directory) if f.endswith('.csv')])
        added_file_paths = new_file_paths - file_paths
        for file_path in added_file_paths:
            # Read the CSV file using pandas
            data = pd.read_csv(file_path, names=['VibX', 'VibY', 'Time'])

        # only give me new data when new data comes into the file.

        file_paths = new_file_paths


def main():
    # Replace '/path/to/your/csv/files' with the actual path to the directory you want to watch
    watch_for_new_csv_files('C:\\')


# Call the main function when the script is run
if __name__ == "__main__":
    main()
