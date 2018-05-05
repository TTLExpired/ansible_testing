# A work in progress, Python renderer for IOS devices
from jinja2 import Environment, FileSystemLoader
import yaml

# Lets load Jinja Template
ENV = Environment(loader=FileSystemLoader('.'), trim_blocks=True,
                  lstrip_blocks=True)
template = ENV.get_template('C_T_IOS.j2')

# Lets load Yaml Global DATA
with open("C_Y_G_IOS.yml", 'r') as ymldata:
    SwGlobal = yaml.load(ymldata)

# We loaded both, lets render the file
print(template.render(SwGlobal))
