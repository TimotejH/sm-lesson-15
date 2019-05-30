
from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route ("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year
    cities = ["Ljubljana", "Kranj", "Koper", "Ptuj"]
    logged_in = True
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities, logged_in=logged_in)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("message")
    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

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