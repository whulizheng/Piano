import librosa
import json
import numpy as np


def LoadFile(file_path):
    y, _ = librosa.load(file_path)
    return y


def Readans(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    return data


def readjson(address):
    with open(address, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict
