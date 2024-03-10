from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import os
import json

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

username_email = {}
email = {}

def datarouterresponse():
    response = make_response("response", 204)
    return response

def token():
    # Assuming the data is sent as form data
    form_data = request.form

    # Check for the specific conditions in the form data
    if form_data.get('grant_type') == 'client_credentials':
        json_file_path = os.path.join(parent_dir, "responses/account/token.json")
        with open(json_file_path, 'r') as static_account_file:
            data = json.load(static_account_file)
        return data

    elif form_data.get('grant_type') == 'password' and 'username' in form_data and 'password' in form_data and form_data.get('includePerms') == 'true':
        # Extract username from email
        global email
        email = form_data['username']
        global username_email
        username_email = email.split('@')[0]

        # Create the JSON response
        json_response = {
            "access_token": "eg1~h1e35h4tr5h456r4h75r4h8r4h5r45h4r5",
            "expires_in": 28800,
            "expires_at": "2050-01-01T00:00:00.000Z",
            "token_type": "bearer",
            "refresh_token": "hjbehjiptjhioptrjhiojeroih",
            "refresh_expires": 86400,
            "refresh_expires_at": "2050-01-01T00:00:00.000Z",
            "account_id": "r54hre45h4r5th48r5hrhr54h56rhr",
            "client_id": "he454e5h48te77h48eh",
            "internal_client": True,
            "client_service": "fortnite",
            "displayName": f"{username_email}",
            "app": "fortnite",
            "in_app_id": "r54hre45h4r5th48r5hrhr54h56rhr",
            "device_id": "he75h4et7hr52h"
        }

        # Respond with the JSON response and 200 status
        return jsonify(json_response), 200

    else:
        # Respond with an error or handle other cases as needed
        return 'Invalid request data', 400
    
def externalauths():
    path = os.path.join(parent_dir, "responses/account/externalAuth.json")
    with open(path, "r", encoding="utf-8") as externalAuthsResponse:
        data = json.load(externalAuthsResponse)
    return data

def account():
    # Assuming the data is sent as form data
    global username_email
    global email

    # Create the JSON response
    json_response = {
        "id": "r54hre45h4r5th48r5hrhr54h56rhr",
        "displayName": f"{username_email}",
        "name": f"{username_email}",
        "email": f"{email}",
        "failedLoginAttempts": 0,
        "lastLogin": "2020-01-01T00:00:00.000Z",
        "numberOfDisplayNameChanges": 0,
        "ageGroup": "UNKNOWN",
        "headless": "false",
        "country": "US",
        "lastName": "Server",
        "preferredLanguage": "en",
        "canUpdateDisplayName": "false",
        "tfaEnabled": "false",
        "emailVerified": "true",
        "minorVerified": "false",
        "minorExpected": "false",
        "minorStatus": "NOT_MINOR",
        "cabinedMode": "false",
        "hasHashedEmail": "false"
        }

        
    return jsonify(json_response), 200

def enabled_features():
    path = os.path.join(parent_dir, "responses/account/enabledFeatures.json")
    with open(path, "r", encoding="utf-8") as enabledFeatures:
        data = json.load(enabledFeatures)
    return data

def cloudstorage():
    path = os.path.join(parent_dir, "responses/account/cloudstorage.json")
    with open(path, "r", encoding="utf-8") as enabledFeatures:
        data = json.load(enabledFeatures)
    return data

def query_profile():
    profile_id = request.args.get('profileId')
    rvn = request.args.get('rvn')

    if profile_id == 'common_public' and rvn == '-1':
        response_file = 'PublicQuery.json'
    elif profile_id == 'common_core' and rvn == '-1':
        response_file = 'CoreQuery.json'
    else:
        response_data = {
            'status': 'error',
            'message': 'Invalid profileId or rvn values'
        }
        return jsonify(response_data)

    response_path = os.path.join(parent_dir, "responses/account", response_file)

    if not os.path.exists(response_path):
        response_data = {
            'status': 'error',
            'message': 'Response file not found'
        }
        return jsonify(response_data)

    with open(response_path, 'r') as file:
        response_data = json.load(file)

    return jsonify(response_data)

def receipts():
    path = os.path.join(parent_dir, "responses/account/receipts.json")
    with open(path, "r", encoding="utf-8") as receiptsResponse:
        data = json.load(receiptsResponse)
    return data

def friends():
    path = os.path.join(parent_dir, "responses/account/friends.json")
    with open(path, "r", encoding="utf-8") as friendResponse:
        data = json.load(friendResponse)
    return data

def block():
    path = os.path.join(parent_dir, "responses/account/blocklist.json")
    with open(path, "r", encoding="utf-8") as blockResponse:
        data = json.load(blockResponse)
    return data

def verify():
    path = os.path.join(parent_dir, "responses/account/verify.json")
    with open(path, "r", encoding="utf-8") as verifyResponse:
        data = json.load(verifyResponse)
    return data

def setmtx():
    path = os.path.join(parent_dir, "responses/account/setmtx.json")
    with open(path, "r", encoding="utf-8") as setmtxResponse:
        data = json.load(setmtxResponse)
    return data