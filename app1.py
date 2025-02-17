from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    name = "Tran Ngoc Huan"  
    birthday = "14.01.2000"
    nationality = "Vietnam"  
    return render_template('profile1.html', name=name, birthday=birthday, nationality=nationality)

if __name__ == '__main__':
    app.run(debug=True, port=5000)