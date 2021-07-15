from flask import Flask, render_template, json, request,redirect,session,jsonify

from flask import Flask
import object_fake_new
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('addWish.html')

@app.route('/addWish',methods=['POST'])
def addWish():
    try:
        _description = request.form['inputDescription']
        if object_fake_new.checkObject(_description):
            return render_template('error.html',error = 'TIN THẬT')
        else:
             return render_template('error.html',error = 'TIN GIẢ')
    except Exception as e:
        return render_template('error.html',error = str(e))
if __name__ == '__main__':
    app.run(port=5002)