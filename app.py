from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cources',methods=['GET'])
def products():
    return 'We have this products!!'

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/home/pythondetails')
def pythondetails():
    return render_template('pythondtl.html')

@app.route('/home/salesforcedetails')
def salesforcedetails():
    return render_template('salesforcedtl.html')

@app.route('/home/manualtestingdetails')
def manualtestingdetails():
    return render_template('manualtestingdtl.html')

@app.route('/home/automationtestingdetails')
def automationtestingdetails():
    return render_template('automationdtl.html')
if __name__ == "__main__":
    app.run(debug=True, port=8000)