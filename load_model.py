from flask.templating import render_template
import joblib
from flask import Flask, request

#instance of an app
app = Flask(__name__)

#Load a model
model = joblib.load('diabetic_79.pkl')

# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
@app.route('/')
def main():
    return render_template('landing.html')

@app.route('/diabetic')
def diabetic():
    return render_template('Diabetic.html')

@app.route('/diabetic_prediction', methods = ['POST'])
def diabetic_prediction():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    print(preg, plas, pres, skin, test, mass, pedi, age)
    
    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if result[0] == 0:
        result = 'Not a diabetic'
    else:
        result = 'Diabetic'
    return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)

