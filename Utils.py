import librosa
import json


def LoadFile(self, file_path):
    y, _ = librosa.load(file_path)
    return y

def readjson(address):
    with open(address, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict