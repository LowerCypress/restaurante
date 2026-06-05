from flask import Blueprint, redirect, render_template, request, url_for

from db import get_connection
edicion1_bp = Blueprint('edicion1', __name__)

@edicion1_bp.route('/editar_pedido/<int:id>', methods=['GET', 'POST'])
def editar_pedido(id):
    conn = get_connection()
    pedido = conn.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        opcion = request.form['opciones']
        conn.execute("UPDATE usuarios  SET nombre = ?, apellido = ?, email = ?, opcion = ? WHERE id = ?", (nombre, apellido, email, opcion, id))
        conn.commit()
        conn.close()
        return redirect(url_for('pedidos'))
    
    conn.close()
    return render_template('editar.html', pedido=pedido)

@edicion1_bp.route('/eliminar_pedido/<int:id>', methods=['POST'])
def eliminar_pedido(id):
    conn = get_connection()
    conn.execute('DELETE FROM usuarios WHERE id = ?', (id,)) 
    conn.commit()
    conn.close()
    return redirect(url_for('pedidos'))