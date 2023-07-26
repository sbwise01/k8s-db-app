#!/usr/bin/env python

import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')

def main(u_path):
    host = os.getenv('PGHOST')
    dbname = os.getenv('PGDATABASE')
    port = os.getenv('PGPORT')
    user = os.getenv('PGUSER')
    password = os.getenv('PGPASSWORD')

    conn = psycopg2.connect(f"host={host} port={port} dbname={dbname} user={user} password={password} target_session_attrs=read-write")
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.people;")
    records = cur.fetchall()
    output = []
    output.append("Hello World ... welcome to Flask with psycopg!  Path=%s" % (u_path))
    for record in records:
        output.append("     %s %s" % (record[0], record[1]) )
    output.append("")

    return "\n".join(output)

if __name__ == "__main__":
    app.run()
