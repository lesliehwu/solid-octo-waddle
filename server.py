from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key="billshouzz"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = ""
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process():

    if request.form["building"] == "farm":
        added = random.randrange(10,21)
        session['gold'] += added
        activity = "\n" + "\nEarned " + str(added) + " golds from the farm! (" + str(datetime.now()) + ")"
        session['activities'] += activity
    
    elif request.form["building"] == "cave":
        added = random.randrange(5,11)
        session['gold'] += added
        activity = "\nEarned " + str(added) + " golds from the cave! (" + str(datetime.now()) + ")\n"
        session['activities'] += activity
    
    elif request.form["building"] == "house":
        added = random.randrange(2,6)
        session['gold'] += added
        activity = "\nEarned " + str(added) + " golds from the house! (" + str(datetime.now()) + ")\n"
        session['activities'] += activity
        
    elif request.form["building"] == "casino":
        added = random.randrange(-50,51)
        session['gold'] += added
        if added < 0:
            activity ="\nLost " + str(added) + " golds from the casino... RIP you (" + str(datetime.now()) + ")\n"
        else:
            activity = "\nEarned " + str(added) + " golds from the casino! (" + str(datetime.now()) + ")\n"
        session['activities'] += activity

    return redirect('/')


app.run(debug = True)
