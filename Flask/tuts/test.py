from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def user():
	first_name = "Jake"
	age = 89
	return render_template('index.html', first_name = first_name, age = age)

if __name__ == "__main__":
	app.run()