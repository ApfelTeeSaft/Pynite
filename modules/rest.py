from flask import Flask
from flask_cors import CORS
import os
import json

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

def calendar():
    path = os.path.join(parent_dir, "responses/rest/calendar.json")
    with open(path, "r", encoding="utf-8") as calendarresponse:
        data = json.load(calendarresponse)
    return data

def versioncheck():
    path = os.path.join(parent_dir, "responses/rest/version.json")
    with open(path, "r", encoding="utf-8") as calendarresponse:
        data = json.load(calendarresponse)
    return data

def statuscheck():
    path = os.path.join(parent_dir, "responses/rest/status.json")
    with open(path, "r", encoding="utf-8") as statusresponse:
        data = json.load(statusresponse)
    return data