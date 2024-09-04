from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "lkjshfiusddfuossb"

@app.route('/nine')
def index():
    flash("tell the name")
    return render_template("index.html")


# @app.route('/greet', methods = ["POST", "GET"])
# def greet():
#     flash("hi" + " " + str(request.form['name_input']))
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)