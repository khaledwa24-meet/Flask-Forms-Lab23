from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


# username = "siwarha"
# password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

user_credentials = {
    "john": "john123",
    "alice": "alice456",
    "bob": "bob789",
    "fouad": "fouad2023",
    "emily": "emily2023",
    "siwarha" : "123"
    }

@app.route('/' , methods=['GET', 'POST']) # '/' for the default page
def login():
	if request.method == "GET" :
		return render_template('login.html')
	else: 
		if (request.form["username"] in user_credentials and request.form["password"] == user_credentials[request.form["username"]]):
			return render_template('home.html', facebook_friends = facebook_friends, user_credentials = user_credentials)
	return redirect(url_for('home'))



@app.route('/friend_exists/<string:name>')
def friend_exists_check(name):
		return render_template('friend_exists.html', facebook_friends = facebook_friends, name = name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
