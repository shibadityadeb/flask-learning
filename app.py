#flask app routing

from flask import Flask,render_template,request,redirect,url_for
#create a simple application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "welcome to my flask app"

@app.route("/index",methods=["GET"])
def index():
    return "welcome to the index page"
#variable routing
@app.route('/success/<float:score>')
def success(score):
    return "the person has passed and the score is "+ str(score)

@app.route('/failure/<float:score>')
def failure(score):
    return "the person has failed and the score is "+ str(score)
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        history=float(request.form["history"])
        avg=(maths+science+history)/3
        res=""
        if avg>=50:
            res= "success"
        else:
            res= "failure"
        return redirect(url_for(res,score=avg))
        # return render_template("form.html",average_marks=avg)
if __name__=="__main__":
    app.run(debug=True)