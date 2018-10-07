# A small script from Cisco to getting source and destination IP
import argparse

parser = argparse.ArgumentParser()

# Command line stuff
parser.add_argument('source_ip', help = 'Source IP address')
parser.add_argument('destination_ip', help = 'Destination IP address')
args = parser.parse_args()

# Get source and destination addresses
source_ip = args.source_ip
destination_ip = args.destination_ip