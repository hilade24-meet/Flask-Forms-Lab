from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Hila"
password = "123"
facebook_friends= ["Refael", "Shlomit", "Tehila", "Noam"]


@app.route('/' , methods= ['GET' , 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST': 
		user= request.form['username']
		pasw= request.form['password']
		if user == username and pasw == password:
			return redirect(url_for('home'))
	
	return render_template('login.html')
		
	
	
@app.route('/home')
def home():
	return render_template('home.html' , frnds=facebook_friends)

	
@app.route('/friend_exists/<string:name>' , methods= ['GET' ,'POST'])
def friend(name):
	return render_template('friend_exists.html', name=name, frnds=facebook_friends)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)