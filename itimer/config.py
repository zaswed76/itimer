import json

def get_config(pth):
    with open(pth, "r") as f:
        return json.load(f)

def save_cfg(pth, data):
    with open(pth, 'w') as outfile:
        json.dump(data, outfile)

class Config:
    def __init__(self):
        self.__data = {}

    def load(self, pth):
        self.__data = get_config(pth)

    def save(self, pth, data):
        save_cfg(pth, data)

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return self.__class__.__name__ + str(self.__data)