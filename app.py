#flask app routing

from flask import Flask
#create a simple application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "welcome to my flask app"

@app.route("/index",methods=["GET"])
def index():
    return "welcome to the index page"
#variable routing
@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the score is "+ str(score)

if __name__=="__main__":
    app.run(debug=True)