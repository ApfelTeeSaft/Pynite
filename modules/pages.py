from flask import Flask
from flask_cors import CORS
import os
import json

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

def fortnitegame():
    path = os.path.join(parent_dir, "responses/pages/fortnite-game.json")
    with open(path, "r", encoding="utf-8") as fortnitegamepage:
        data = json.load(fortnitegamepage)
    return data