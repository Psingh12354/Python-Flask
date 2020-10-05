from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/bootstrap")
def priyanshu():
    return render_template('bootstap.html')
app.run(debug=True)