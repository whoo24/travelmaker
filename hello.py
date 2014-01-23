from flask import Flask, render_template

app = Flask(__name__)
app.debug = True;

@app.route("/")
def hello():
	#return "Hello World!"
	return render_template('map.html', name=None)

if __name__ == "__main__":
	app.run()
