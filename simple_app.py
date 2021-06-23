"""
service to query the video game URL
"""

from flask import Flask,request,redirect,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def input():
   if request.method == 'POST':
      id = request.form['id']
      link = 'https://www.freetogame.com/api/game?id='+id
      return redirect(link)
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
