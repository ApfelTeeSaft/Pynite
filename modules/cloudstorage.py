from flask import Flask, send_file
from flask_cors import CORS
import os
import json

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

def system():
    path = os.path.join(parent_dir, "responses/cloudstorage/system.json")
    with open(path, "r", encoding="utf-8") as calendarresponse:
        data = json.load(calendarresponse)
    return data

def defaultengine():
    path = os.path.join(parent_dir, "config/DefaultEngine.ini")
    content_type = "text/plain"
    return send_file(path, mimetype=content_type)

def defaultgame():
    path = os.path.join(parent_dir, "config/DefaultGame.ini")
    content_type = "text/plain"
    return send_file(path, mimetype=content_type)

def defaultruntime():
    path = os.path.join(parent_dir, "config/DefaultRuntimeOptions.ini")
    content_type = "text/plain"
    return send_file(path, mimetype=content_type)