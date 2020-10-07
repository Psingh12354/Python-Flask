from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index3.html')

@app.route("/about")
def contact():
    return render_template('about.html')

app.run(debug=True)