import os
import time
import csv
import socket
import json


def watch_for_new_csv_files(directory):
    """
    Watches for new CSV files in the specified directory and loads the contents
    into a dictionary with three keys corresponding to the three columns.
    """
    file_paths = set()
    while True:
        # Get a list of all CSV files in the directory
        new_file_paths = set([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])

        # Check if any new files have appeared
        added_file_paths = new_file_paths - file_paths
        for file_path in added_file_paths:
            # Open the new file and load its contents into a dictionary
            with open(file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                dict_items = [{row[0]: row[1], row[2]: row[3], row[4]: row[5]} for row in reader]
                c = dict_items[]

            # Do something with the dictionary items (e.g., print them)
            m = model_selection(c)
            f = signal_processing(m, dict_items)

            
            state, probability = model(m,p,f1)

            dict_to_send = {'state': state, 'probability': probability}

            send_to_udp_server(dict_to_send)
            

        file_paths = new_file_paths
        time.sleep(1)

def send_to_udp_server(msg_to_send):
    """
    Sends a message to the UDP server.
    """
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = json.dumps(msg_to_send)

    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def signal_processing(dict_items):
    print(dict_items)


def model_selection(dict_items):
    print(dict_items)
      
def model(kl,p,f1):
    print(kl,p,f1)

    return (state, probablity)



