from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def user():
	first_name = "Jake"
	return render_template('index.html', first_name = first_name)

if __name__ == "__main__":
	app.run()