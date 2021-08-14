#import a library
from flask import Flask, render_template, request

#instance of an app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/data', methods = ['POST'])
def data():
    first_name = request.form.get('FirstName')
    last_name = request.form.get('LastName')
    phn_num = request.form.get('PhoneNumber')
    email = request.form.get('Email')

    print(first_name, last_name, phn_num, email)
    return 'form submitted.'

if __name__ == '__main__':
    app.run(debug = True)