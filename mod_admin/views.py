from flask import session , render_template , request , abort
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin 

@admin.route('/')
def index():
	return "Hello from Admin"


@admin.route('/login/', methods=['GET' , 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		if not form.validate_on_submit():
			abort(400)
	    # user = User.query.filter( User.email == form.email.data ).first()
		user = User.query.filter(User.email.ilike(f'form.email.data')).first()
		if not user:
			return "Incorect Credentials" , 400 
		if not user.check_password(form.password.data):
		    return "incorrect password "
		session['email'] = user.email
		session['id'] = user.id
		return "You Logged in successfully"	
	if session.get('email') is not None:
		return "You are Already Logged in"		
	return render_template('admin/login.html',form=form) 
    	

	