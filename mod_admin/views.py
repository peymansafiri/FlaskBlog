from flask import session
from . import admin 

@admin.route('/')
def index():
	return "Hello from Admin"


@admin.route('/login/')
def login():
	session['name']= 'Peyman'
	print(session.get('name'))
	print(session)
	return "Hello from login"
