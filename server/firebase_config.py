import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

key_dict = json.loads(os.getenv("FIREBASE_KEY_JSON"))
cred = credentials.Certificate(key_dict)

firebase_admin.initialize_app(cred)

db = firestore.client()