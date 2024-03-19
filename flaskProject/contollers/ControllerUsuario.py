from flask import Blueprint, request, render_template, flash, url_for
from model import model_usuario

blueprint_user = Blueprint('user', __name__, url_prefix='/user')

@blueprint_user.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        name = request.form['name'] or None
        last_name = request.form['last_name'] or None
        password = request.form['password'] or None
        email = request.form['email'] or None
        is_admin = request.form['is_admin'] or None
        
        is_admin_user = is_admin == 'yes'

        try:
            model_usuario.add_user(name, last_name, password, email, is_admin_user)
            return render_template('result.html', title="Add User", result="User added successfully :)")
        except Exception as e:
            print(e)
            return render_template('result.html', title="Add User", result="An error occurred while adding the user :(")


@blueprint_user.route('/view', methods=['GET'])
def view_users():
    try:
        users = model_usuario.get_users()
        return render_template('view_users.html', users=users)
    except Exception as e:
        print(e)
        return render_template('result.html', title="View Users", result="An error occurred while viewing users :/")


@blueprint_user.route('/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        return render_template('update_user.html')
    else:
        user_id = request.form['id'] or None
        name = request.form['name'] or None
        last_name = request.form['last_name'] or None
        password = request.form['password'] or None
        email = request.form['email'] or None
        is_admin = request.form['is_admin']

        is_admin_user = is_admin == 'yes'

        try:
            model_usuario.update_user(user_id, name, last_name, password, email, is_admin_user)
            return render_template('result.html', title="Crear usuario", result="Usuario agregado")
        except Exception as e:
            print(e)
            return render_template('result.html', title="Crear usuario", result="Algo salió mal")


@blueprint_user.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        return render_template('delete_user.html')
    else:
        user_id = request.form['user_id'] or None

        try:
            model_usuario.delete_user(user_id)
            return render_template('result.html', title="Borrar usuario", result="User deleted successfully :)")
        except Exception as e:
            print(e)
            return render_template('result.html', title="Borrar usuario", result="An error occurred while deleting the user :(")
