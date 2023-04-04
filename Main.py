import os
import time
import csv
import socket
import json
import math
import pandas as pd

#Rename this function DigitalTwin
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
        if last_processed_file_number != highest_file_number:
    
            # Change TEST_ to the prefix of the CSV files you want to process
            file_path = os.path.join(directory, f'TEST_{highest_file_number}.csv')

            # Read the CSV file using pandas
            data = pd.read_csv(file_path, names=[
                               'VibX', 'VibY', 'Time'])  # Data stream
            print(f'Processed {file_path}:')
            # Context States used to represent a system’s current parameters
            c = data['VibX'].tolist()
            p = data['VibY'].tolist()  # Modeling parameters
            f1 = data['Time'].tolist()  # Transformed set of features

            # Data Pre-proecssor block below
            m = model_selection(c)  # model identifier
            f = signal_processing(m, data)  # Features
            p, f1 = context_filtering(c, f, p)

            # Model Bank Below
            state, probability = model(m, p, f1)

            dict_to_send = {'state': state, 'probability': probability}

            send_to_udp_server(dict_to_send)

        # Update the last processed file number
        last_processed_file_number = highest_file_number
        # Adjust the time.sleep() value to control how often the function checks for new files.
        time.sleep(0.1)


# Make sure the funciton below works.
def send_to_udp_server(msg_to_send):
    """
    Sends a message to the UDP server.
    """
    UDP_IP = "192.168.50.3"
    UDP_PORT = 5005
    MESSAGE = json.dumps(msg_to_send).encode('utf-8')

    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE.decode('utf-8'))

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def signal_processing(m, data):
    # Extract the values of the specified column (m) from the data DataFrame
    column_values = data.iloc[:, m].values.tolist()

    # Calculate the square of each value in the column
    squared_values = [value**2 for value in column_values]

    # Calculate the mean of the squared values
    mean_of_squares = sum(squared_values) / len(squared_values)

    # Calculate the root mean square (RMS) value
    rms_value = math.sqrt(mean_of_squares)

    return rms_value


def model_selection(dict_items):
    # Insert model selection code here
    return 1


def context_filtering(dict_items):
    # Insert Context filteirng code here
    print(dict_items)  # placeholder code


def model(kl, p, f1):
    # what is pickling?
    return {'state': "Healthy", 'probability': .85}  # placeholder code


def main():
    # Replace '/path/to/your/csv/files' with the actual path to the directory you want to watch
    directory_to_watch = '/path/to/your/csv/files'
    watch_for_new_csv_files(directory_to_watch)


# Call the main function when the script is run
if __name__ == "__main__":
    main()
