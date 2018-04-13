# A very simple example to reading yaml file 

import yaml
# Open file and assign data to f
with open("vendor_yaml_example.yml") as f:
    # Parse f as per yaml module and assigne value to result
    result = yaml.load(f)
    print(result)
    # Not showing what type result is for some reason!
    type(result)
