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
    last_processed_file_number = -1
    while True:
        # Get a list of all CSV files in the directory
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

        # Extract file numbers and find the highest file number
        file_numbers = [int(f.split('_')[1].split('.')[0]) for f in csv_files]
        highest_file_number = max(file_numbers) if file_numbers else -1

        # Process the new file(s) with a higher number than the last processed file
        for file_number in range(last_processed_file_number + 1, highest_file_number + 1):
            # Change TEST_ to the prefix of the CSV files you want to process
            file_path = os.path.join(directory, f'TEST_{file_number}.csv')

            # Read the CSV file using pandas
            data = pd.read_csv(file_path, names=['VibX', 'VibY', 'Time'])
            print(f'Processed {file_path}:')
            print(data)

        # Update the last processed file number
        last_processed_file_number = highest_file_number
        # Adjust the time.sleep() value to control how often the function checks for new files.
        time.sleep(0.1)


def main():
    # Replace '/path/to/your/csv/files' with the actual path to the directory you want to watch
    watch_for_new_csv_files('C:\\')


# Call the main function when the script is run
if __name__ == "__main__":
    main()
