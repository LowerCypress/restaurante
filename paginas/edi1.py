from flask import Blueprint, redirect, render_template, request, url_for

from db import get_connection
edi1_bp = Blueprint('edi1', __name__)

@edi1_bp.route('/editar_proveedor/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
    conn = get_connection()
    pedido = conn.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        numero = request.form['numero']
        nombre = request.form['nombre']
        email = request.form['email']
        opcion = request.form['opciones']
        conn.execute("UPDATE usuarios  SET numero = ?, nombre = ?, email = ?, opcion = ? WHERE id = ?", (numero, nombre, email, opcion, id))
        conn.commit()
        conn.close()
        return redirect(url_for('proveedores'))
    
    conn.close()
    return render_template('editar_prov.html', pedido=pedido)

@edi1_bp.route('/eliminar_proveedor/<int:id>', methods=['POST'])
def eliminar_proveedor(id):
    conn = get_connection()
    conn.execute('DELETE FROM proveedores WHERE id = ?', (id,)) 
    conn.commit()
    conn.close()
    return redirect(url_for('proveedores'))