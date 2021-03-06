from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


from flask_mail import Mail


with open("config.json", 'r') as file:
    params = json.load(file)['params']

local_server=True

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME= params['gmail_id'],
    MAIL_PASSWORD=params['gmail_password']
    )

mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

# hmnne class ka naam Cotactsislie rakha hai bcz our table name is "contacts"
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12),nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=True)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25),nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")

def home():

    return render_template('index.html', params = params)


@app.route("/post/<string:post_slug>", methods=["GET"])
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html', params = params, post = post)

@app.route("/about")
def about():

    return render_template('about.html', params = params)

@app.route("/contact", methods= ['GET','POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, phone_num=phone, msg=message, date = datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(name + "share post for Jai",
                            sender=email,
                            recipients=[params['gmail_id']],
                            body = message + "\n" + phone
                            )
    return render_template('contact.html', params = params)

app.run(debug=True, port=8001)