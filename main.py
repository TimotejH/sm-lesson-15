from flask import Flask, render_template

app = Flask(__name__)

@app.route ("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/foogle-login")
def foogle():
    return render_template("fakegoogle-login.html")

@app.route("/portfolio/og-barbershop")
def barbershop():
    return render_template("og-barbershop.html")

if __name__ == "__main__":
    app.run(use_reloader=True)