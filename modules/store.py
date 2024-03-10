from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import os
import json

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

def catalog():
    path = os.path.join(parent_dir, "responses/store/catalog.json")
    with open(path, "r", encoding="utf-8") as catalogentry:
        data = json.load(catalogentry)
    return data