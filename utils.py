import json

def load_credentials(filename):
    with open(filename, "r") as file:
        config = json.load(file)
    return config