from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Navgurukul'
db = SQLAlchemy(app)

# hmnne class ka naam Cotactsislie rakha hai bcz our table name is "contacts"

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12),nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=True)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods= ['GET','POST'])
def contact():
    # Add entry to the database
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, phone_num=phone, msg=message, date = datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

app.run(debug=True, port=8001)