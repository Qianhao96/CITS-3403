from functools import wraps
from flask import redirect, url_for, flash, current_app
from flask_login import current_user
import os
import secrets
from PIL import Image

def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if not current_user.is_active:
        # 	flash('Please login as Admin to access this page', 'warning')
        # 	return redirect(url_for('users.login'))
        # elif not current_user.is_admin:
        # 	flash('Please logout and login as Admin to access this page', 'warning')
        # 	return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/image/polls', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def delete_picture(name):
    os.remove(os.path.join(current_app.root_path, 'static/image/polls', name))