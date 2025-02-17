from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # debug=True for local development