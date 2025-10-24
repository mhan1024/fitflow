import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("fitflow_backend/serviceAccountKey.json")
firebase_admin.initialize_app(cred)