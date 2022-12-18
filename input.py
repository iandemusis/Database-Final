from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

##jinja 2 templating

@app.route('/')
def front_page():
    return render_template('front.html')

@app.route('/create')
def create():
    return "some text"

@app.route('/update')
def update():
    return "some text" ##here i dont know how to link to an html of apartments, and some way to update them

@app.route('/erase')
def erase():
    return "some text" ##here i dont know how to link to an html of apartments, and when i click on them they get erased.

@app.route('/list')
def list():
    return "some text" ##here i need to add the list of apartments

@app.route('/', methods = ["POST"])
def create__():
    input_text = request.form["tenant_name"]
    return input_text


def main():
    app.run(debug=True)

if __name__=='__main__':
    main()

##must have create, read, update, delete
