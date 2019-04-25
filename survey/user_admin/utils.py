from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_active:
        	flash('Please login as Admin to access this page', 'warning')
        	return redirect(url_for('users.login'))
        elif not current_user.is_admin:
        	flash('Please logout and login as Admin to access this page', 'warning')
        	return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function