from flask import Flask,render_template,redirect, url_for, request,session
import metadata_parser
import os

app = Flask(__name__)
app.secret_key = 'ashrafMYSecret123456789'

port_num = int(os.environ.get('PORT'))
#port_num = 5000
postLink = f"https://urlmeta.herokuapp.com/"
#postLink = f"http://localhost:5000/"
@app.route('/', methods=['POST', 'GET'])
def login(): 
    if request.method == 'GET':
        return render_template("home.html",portn = postLink)
    if request.method == 'POST':
        try:
            url = request.form['nm']
            page = metadata_parser.MetadataParser(url)
            info = page.metadata
            if info['og'] == {}:
                data = info['meta']
            else:
                data = info['og']
            return render_template('index.html',urlinfo = data,urllink = url,portn = postLink)
        except:
            return "Not an Url"
    


if __name__ == '__main__':
   #secret_key = 'mysecret1234'
   app.run(debug=True,host='0.0.0.0',port=port_num)