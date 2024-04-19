import firebase_admin
from firebase_admin import db, credentials
import json

cred = credentials.Certificate("firebase_credentials.json")
        
firebase_admin.initialize_app(cred, {"databaseURL": "https://dailyupdate-9b7c9-default-rtdb.asia-southeast1.firebasedatabase.app/"})

ref = db.reference("/")

database = db.reference("/users").get()