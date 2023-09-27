from flask import Blueprint, render_template, request, redirect
import controller as c
import json
from random import randint

views = Blueprint('views', __name__)
error = False; 

# Home page - Welcomes user and contains form to initialize practice page
@views.route('/', methods=['POST', 'GET'])
def home():
    # call error if search request yielded no results. 
    global error; 
    if (error):
        error=False
        return render_template("home.html", error="no results")

    # If form submitted 
    if request.method =='POST': 
        c.search = request.form['search']
        c.quantity = request.form['quantity']
        c.interval = request.form['time-interval']
        c.max_page_num = 51 - int(request.form['accuracy'])
        c.sessionID = c.sessionID + 1

        # Check inputted results 
        if c.search =='':
            return render_template("home.html", error="no search query")
        if c.quantity =='':
            return render_template("home.html", error="no quantity")
        if c.interval =='':
            return render_template("home.html", error="no interval")

        return redirect("/practice")
    
    c.results = []

    return render_template("home.html")

# Practice page - Images from APIs are displayed to user in timed intervals 
@views.route('/practice', methods=['POST', 'GET'])
def practice():
    # If there are search results 
    if c.search != None: 
        # Query APIS
        results = c.Handler(c.search, c.quantity, c.max_page_num)

        # Validate results 
        if len(results) <= 0:
            global error
            error = True
            return redirect("/") 
    
        # Organize results
        image = results[0][2]
        sec = c.interval
        c.search, c.quantity, c.interval, c.max_page_num = None, None, None, None

        # Replace single quotes --> ensure string doesn't break 
        for users in results:
            if users[1].find("'"):
                users[1] = users[1].replace("'", "&#39;")

        results_json = json.dumps(results)

        return render_template("practice.html", img = image, seconds=sec, images = results_json, sessionID=c.sessionID)
    elif request.method == 'POST':
        return redirect("/gallery")
    else:
        return render_template("practice.html")
    

   
# Gallery page - displays all the images queried by the api at the end of the session on one page. 
# allows the user to go to the original URL of the image. 
@views.route('/gallery')
def gallery():
    images=json.dumps(c.results)
    return render_template("gallery.html", images=images)
