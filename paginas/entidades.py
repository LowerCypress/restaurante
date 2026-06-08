from flask import Blueprint, redirect, render_template, request, url_for
from db import get_connection

entidades_bp = Blueprint('entidades', __name__)

@entidades_bp.route('/proveedores/agregar', methods=['POST'])
def agregar_proveedores():
    if request.method == 'POST':
        numero = request.form.get('numero')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        producto = request.form.get('opciones')
        
        conn = get_connection()
        conn.execute('''
            INSERT INTO proveedores (numero, nombre, email, producto) 
            VALUES (?, ?, ?, ?)
        ''', (numero, nombre, email, producto))
        conn.commit()
        conn.close()
        return redirect(url_for('entidades.listar_proveedores'))

@entidades_bp.route('/proveedores')
def listar_proveedores():
    conn = get_connection()
    proveedores = conn.execute('SELECT id,numero,nombre,email,producto FROM proveedores').fetchall()
    conn.close()
    return render_template('Proovedores.html', proveedores=proveedores)