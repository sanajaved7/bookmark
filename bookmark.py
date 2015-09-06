from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

from logging import DEBUG

app = Flask(__name__)
app.config['SECRET_KEY'] = '4 \xdb\xde{#TC\xb2\x03A\xd8\xa5\xf5^\xb6.\xb3\x9c\x11\xa1\x8a^/'

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}.{}.".format(self.firstname[0], self.lastname[0])

    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname )

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "sana",
        date = datetime.utcnow()
        ))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title passed from view to template", user=User("Sana", "Javed"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

