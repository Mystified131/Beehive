#This code imports the necessary modules.

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Hivebuilder import blobintophrases

import cgi, datetime, random

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Beehive:Jackson1313@localhost:8889/Beehive'
db = SQLAlchemy(app)
app.secret_key = 'pgojaeopaiern'

#This code sets up the model for the database

class Beehive(db.Model):
    timestamp = db.Column(db.String(120), primary_key=True)
    phrase = db.Column(db.String(120))
    phrasecount = db.Column(db.Integer)

    def __init__(self, timestamp, phrase, phrasecount):
        self.timestamp = timestamp
        self.phrase = phrase
        self.phrasecount = phrasecount

@app.route('/', methods=['POST', 'GET'])
def index():
    #textchunk = request.form["textchunk"]
    textchunk = "testing the workability here. hello, hello"
    phraseset = blobintophrases(textchunk)
    right_now = datetime.datetime.now().isoformat()
    lista = []
    for i in right_now:
        if i.isnumeric():
            lista.append(i)
        tim = "".join(lista)
    timestamp = tim
    for elem in phraseset:
            phrase = elem
            phrasecount = 1
            new_phrase = Beehive(timestamp, phrase, phrasecount)
            db.session.add(new_phrase)
            db.session.commit()
    return render_template('index.html')

    ## THE GHOST OF THE SHADOW ##

if __name__ == '__main__':
    app.run()
