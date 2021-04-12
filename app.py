from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    # headline = "uname has registered"
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']


        # return redirect(url_for("login"))
    return render_template("index.html")



# @app.route('/register',methods=["GET","POST"])
# def register():
#     msg = ''
#     if request.method =="GET":
#         msg = "You have successfully registered."

#     return render_template("index.html")

# @app.route("/bhavana")
# def bhavana():
#    return "Hello, Bhavana!!"

