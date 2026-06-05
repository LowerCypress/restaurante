from flask import Blueprint, redirect, render_template, request, url_for
from db import get_connection

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        opcion = request.form.get("opciones")
        conn = get_connection()
        conn.execute('''
            INSERT INTO usuarios (nombre, apellido, email, opcion)
            VALUES (?, ?, ?, ?)
        ''', (nombre, apellido, email, opcion))
        conn.commit()
        conn.close()
        return redirect(url_for('shop.pedidos'))




    return render_template('pedidos.html')