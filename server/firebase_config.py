import os
import json
import firebase_admin
from firebase_admin import credentials, firestore


if os.path.exists("/etc/secrets/service-account-key.json"):
    secret_file_path = "/etc/secrets/service-account-key.json"
else:
    secret_file_path = "service-account-key.json"

with open(secret_file_path, "r", encoding="utf-8") as file:
    key_dict = json.load(file)

cred = credentials.Certificate(key_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()