import yaml

with open('travis.yml', 'r') as source:
    data = source.read()
    print(yaml.load(data))