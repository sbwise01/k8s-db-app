#!/usr/bin/env python

import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')

def main(u_path):
    host = os.getenv('PGHOST')
    dbname = os.getenv('PGDATABASE')
    port = os.getenv('PGPORT')
    user = os.getenv('PGUSER')
    password = os.getenv('PGPASSWORD')

    webOutput = {}
    webOutput['message'] = "Hello World ... welcome to Flask with psycopg!"
    webOutput['people'] = []

    conn = psycopg2.connect(f"host={host} port={port} dbname={dbname} user={user} password={password} target_session_attrs=read-write")
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.people;")
    records = cur.fetchall()
    for record in records:
        person = {}
        person['first_name'] = record[0]
        person['last_name'] = record[1]
        webOutput['people'].append(person)

    return jsonify(**webOutput)

if __name__ == "__main__":
    app.run()
