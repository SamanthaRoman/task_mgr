import sqlite3
from flask import g

DATABASE_URL = "main.db"        #constant variable that won't be deleted when used.

def get_db():
    db = getattr(g, "_database", None)
    if not db:      #if db == None
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db