from http.client import OK
from flask import Flask,abort,render_template,request,redirect,url_for, jsonify
import os

import init
from db_service import DbService

app = init.init_app()
db_service = DbService(app)

@app.route('/query')
def query():
   surname = request.args.get('surname')

   return '''<h1>The surname value is: {}</h1>'''.format(surname)

#TODO EXAMPLE
@app.rout('/cats', methods=['GET', 'POST'])
def cat_request():
   if request.method =='POST':
      body_data = request.json
      return OK
   else:
      body_data = request.json
      cat_id = body_data['name']
      #if no cats specified return all
      return jsonify(db_service.get_cats())
      #else return specific
      return jsonify(db_service.get_cat(cat_id))


@app.route('/success/<name>')
def success(name):
   return 'welcome, %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))




@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
   if request.method =='POST':
      file = request.files['file[]']
      if file:
         filename = file.filename
         file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
         return "The file is uploaded"
   return render_template('upload.html')


if __name__ == '__main__':
   app.run()