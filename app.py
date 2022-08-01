from Rewriter import Rewriter
from pymongo import MongoClient
import json

import os 
import random 
import string

from flask import Flask,render_template,url_for,request,flash,jsonify

templates = os.path.join(os.getcwd(),"templates/")

app = Flask(__name__, template_folder=templates)

app.config['SECRET_KEY'] = "secrestsArePrivate"

client = MongoClient(os.environ.get("MONGO_URL"))

db = client["rewiter"]

collection = db["api"]



@app.route("/",methods=['POST','GET'])

def index():

    text = request.form.get("text")

    print(text)
    

    if text != None:

        rewriter = Rewriter(text)

        rewritten = rewriter.main()[0]

        return render_template("index.html",retext=rewritten,originaltxt=text)

    return render_template("index.html")
  

@app.route("/v1/api")

def api():

    text = request.args.get("text", default = "*", type = str)

    apikey = request.args.get("apikey", default = "NOAPI", type = str)

        if collection.find_one({"apikey": apikey}):

            if text != "*" and apikey != "NOAPI":

                rewriter = Rewriter(text)

                rewritten = rewriter.main()[0]

                return jsonify(status="Successful", text=rewritten, author="Vaibhav Chandra")

            else:

                return jsonify(status="Unsuccessful", text=None, author="Vaibhav Chandra")

        else:

            return jsonify(status="Unsuccessful", text="Provide an Valid API Key!", author="Vaibhav Chandra")
 








@app.route("/api_key", methods=["GET", "POST"])

def api_key():

    name = request.form.get("name")

    email = request.form.get("email")

    apikey = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))

    if request.method in ["POST", "GET"]:

        if "name" in request.form and "email" in request.form:

            doc = {"name": name, "email": email, "apikey" : apikey}

            if collection.find_one({"email": email}) == None:

                flash("API Key Generated Successfully!")

                return render_template("api.html",apikey=apikey)

            else:

                flask("Email Already Registered")

                return render_template("api.html")

                

    return render_template("api.html")



@app.errorhandler(404)

def not_found(e):

    return render_template("404.html")
    
    
if __name__ == "__main__":

    # debug = true will enable the debugger

    app.run(debug=True)

