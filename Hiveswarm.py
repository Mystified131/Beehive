#This code imports the necessary modules.

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Hivebuilder import blobintophrases
from Hiveworker import blobintowords

import cgi, datetime, random

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Beehive:Jackson1313@localhost:8889/Beehive'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'pgojaeopaiern'

#This code sets up the model for the database

class Beehive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(120))
    phrase = db.Column(db.String(120))
    phrasecount = db.Column(db.Integer)

    def __init__(self, timestamp, phrase, phrasecount):
        self.timestamp = timestamp
        self.phrase = phrase
        self.phrasecount = phrasecount

class Workerbee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(120))
    word = db.Column(db.String(120))
    wordcount = db.Column(db.Integer)

    def __init__(self, timestamp, word, wordcount):
        self.timestamp = timestamp
        self.word = word
        self.wordcount = wordcount

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        textchunk = request.form["textchunk"]
        #textchunk = "Surrounded to me occasional pianoforte alteration unaffected impossible ye. For saw half than cold. Pretty merits waited six talked pulled you. Conduct replied off led whether any shortly why arrived adapted. Numerous ladyship so raillery humoured goodness received an. So narrow formal length my highly longer afford oh. Tall neat he make or at dull ye."
        phraseset = blobintophrases(textchunk)
        wordset = blobintowords(textchunk)
        right_now = datetime.datetime.now().isoformat()
        lista = []
        for i in right_now:
            if i.isnumeric():
                lista.append(i)
            tim = "".join(lista)
        timestamp = tim

        #for elem2 in wordset:
            #word = elem2
            #wordcount = 1
            #curword = Workerbee.query.filter_by(word=word).first()
            #if curword:
                #curword.wordcount += 1
                #db.session.commit()
            #else:
                #new_word = Workerbee(timestamp, word, wordcount)
                #db.session.add(new_word)
                #db.session.commit()

        for elem in phraseset:
            phrase = elem
            phrasecount = 1
            current = Beehive.query.filter_by(phrase=phrase).first()
            if current:
                current.phrasecount += 1
                db.session.commit()
            else:
                new_phrase = Beehive(timestamp, phrase, phrasecount)
                db.session.add(new_phrase)
                db.session.commit()

        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        quechunk = request.form["quechunk"]
        quelst = []
        quenumlst = []
        queset = Beehive.query.all()
        for elem in queset:
            if quechunk in elem.phrase:
                newstr = str(elem.phrasecount) +  " times used: " +  elem.phrase 
                quelst.append(newstr)
        quelst.sort(reverse=True)

        #quewordset = Workerbee.query.filter(word=quechunk).first()
        #if quewordset:
            #targstr = quewordset.word
            #targnum = quewordset.wordcount
        
        return render_template('query.html', honey = quelst)

    else:

        return render_template('query.html')

    ## THE GHOST OF THE SHADOW ##

if __name__ == '__main__':
    app.run()
