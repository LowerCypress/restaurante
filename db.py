import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for, session


def get_connection():
    conn = sqlite3.connect('usuarios.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    opcion TEXT NOT NULL
        ) 
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    numero TEXT NOT NULL,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    producto TEXT NOT NULL
        )
    ''')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cuentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            rol TEXT DEFAULT 'user'
        )
    """)

    existe = conn.execute("SELECT * FROM cuentas WHERE username=?", ('admin',)
    ).fetchone() 
    if existe is None:
        conn.execute("INSERT INTO cuentas (username, password, rol) VALUES (?, ?, ?)", ('admin', '1234', 'admin'))

    existe = conn.execute("SELECT * FROM cuentas WHERE username=?", ('chef',)
    ).fetchone() 
    if existe is None:
        conn.execute("INSERT INTO cuentas (username, password, rol) VALUES (?, ?, ?)", ('chef', '4321', 'chef'))
    conn.commit()
    conn.close()