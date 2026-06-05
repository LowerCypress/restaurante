import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for, session
from db import get_connection, init_db
from paginas import create_app

app = create_app()
app.secret_key = 'cambiar_esta_clave'

    # ---------------------------------------
# Login y Logout
# ---------------------------------------


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        try:
            conn.execute("INSERT INTO cuentas (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash('Registro exitoso', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El usuario ya existe', 'danger')
        finally:
            conn.close()

    return render_template('register.html')


@app.before_request
def require_login():
    allowed = ('login', 'register', 'static')
    if request.endpoint in allowed:
        return
    if 'username' not in session:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        user = conn.execute("SELECT * FROM cuentas WHERE username=? AND password=?", (username, password)).fetchone()
        conn.close()

        if user:
            session['username'] = username
            session['rol'] = user['rol']
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio.inicio'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Eliminamos los datos del usuario de la sesión actual
    session.pop('username', None)
    session.pop('rol', None)
    
    # Opcional: mostrar un mensaje de que se cerró sesión
    flash('Has cerrado sesión correctamente.', 'info')
    
    # Redirigimos de vuelta al login
    return redirect(url_for('login'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)