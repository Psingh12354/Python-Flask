from flask import Flask, render_template
app = Flask(__name__)
@app.route('/') #use to define end point(/)
def hello():
    return render_template('index.html')
app.run()  #to run on local host

