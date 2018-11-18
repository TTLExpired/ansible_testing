import os
import json
import glob

file_list = glob.glob('*')

# Let's print a dictionary with filenames and sizes:
data = {x: os.stat(x).st_size for x in file_list if '__' not in x}

print(data)

