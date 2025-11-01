import json
import random
import os

# Ruta del archivo JSON
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "pokeneas.json")

# Cargar los pokeneas desde el archivo
with open(DATA_PATH, "r", encoding="utf-8") as file:
    pokeneas = json.load(file)

def pokenea_random():
    return random.choice(pokeneas)
