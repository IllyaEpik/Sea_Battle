import os
import json
def find_file(name_file):
    file = __file__.split("\\")
    del file[-1]
    del file[-1]
    return os.path.join("/".join(file),name_file)
def create_json(dict,name_file):
    with open(find_file(f"json/{name_file}.json"),"w") as file:
        json.dump(dict,file)
def read_json(name_file):
    with open(find_file(f"json/{name_file}.json")) as file:
        return json.load(file)