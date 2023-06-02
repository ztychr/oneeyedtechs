from flask import Flask, request
from flask import render_template
from urllib.parse import urlparse

app = Flask(__name__)

@app.before_request
def get_host():
    global host
    if (request.headers.get('Host') == "oneeyedtechs.com"):
        host = "One Eyed Techs"
    elif (request.headers.get('Host') == "www.nordskov.net"):
        host = "Nordskov Blog"
    else:
        host = "One Eyed Techs"

@app.route("/")
def index():
    return render_template('index.html', name='index', host=host)

@app.route("/about")
def about():
    return render_template('about.html', name='about', host=host)

@app.route("/post/certificate-length")
def certificate_length():
    return render_template('certificate-length.html', name='certificate-length', host=host)

@app.route("/post/rejsekortet-an-obsolete-smart-card")
def rejsekortet_an_obsolete_smart_card():
    return render_template('rejsekortet-an-obsolete-smart-card.html', name='rejsekortet-an-obsolete-smart-card', host=host)

@app.route("/post/nfc-payment-roskilde-festival")
def nfc_payment_roskilde_festival():
    return render_template('nfc-payment-roskilde-festival.html', name='nfc-payment-roskilde-festival', host=host)

@app.route("/post/htb-curling")
def htb_curling():
    return render_template('htb-curling.html', name='htb-curling', host=host)

@app.route("/post/htb-jerry")
def htb_jerry():
    return render_template('htb-jerry.html', name='htb-jerry', host=host)

@app.route("/post/htb-poison")
def htb_poison():
    return render_template('htb-poison.html', name='htb-poison', host=host)

#@app.route("/post/case-competition")
#def case_competition():
#    return render_template('case-competition.html', name='case-competition', host=host)
