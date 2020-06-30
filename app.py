from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/blog_detail')
def blog_detail():
    return render_template("blog_detail.html")

if __name__=='__main__':
    app.run(debug=True)