from Rewriter import Rewriter

import json

import os

from flask import Flask,render_template,url_for,request,flash,jsonify

templates = os.path.join(os.getcwd(),"templates/")

app = Flask(__name__, template_folder=templates)

app.config['SECRET_KEY'] = "secrestsArePrivate"



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

    if text != "*":

        rewriter = Rewriter(text)

        rewritten = rewriter.main()[0]

        return jsonify(status="Successful", text=rewritten, author="Vaibhav Chandra")

    else:

        return jsonify(status="Unsuccessful", text=None, author="Vaibhav Chandra")


@app.errorhandler(404)

def not_found(e):

    return render_template("404.html")
    
    
if __name__ == "__main__":

    # debug = true will enable the debugger

    app.run(debug=True)

