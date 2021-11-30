from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', name='index')

@app.route("/about")
def about():
    return render_template('about.html', name='about')

@app.route("/post/rejsekortet-an-obsolete-smart-card")
def rejsekortet_an_obsolete_smart_card():
    return render_template('rejsekortet-an-obsolete-smart-card.html', name='rejsekortet-an-obsolete-smart-card')

@app.route("/post/nfc-payment-roskilde-festival")
def nfc_payment_roskilde_festival():
    return render_template('nfc-payment-roskilde-festival.html', name='nfc-payment-roskilde-festival')

@app.route("/post/htb-curling")
def htb_curling():
    return render_template('htb-curling.html', name='htb-curling')

@app.route("/post/htb-jerry")
def htb_jerry():
    return render_template('htb-jerry.html', name='htb-jerry')

@app.route("/post/htb-poison")
def htb_poison():
    return render_template('htb-poison.html', name='htb-poison')

@app.route("/post/case-competition")
def case_competition():
    return render_template('case-competition.html', name='case-competition')
