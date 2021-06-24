"""
service to query the video game URL
"""

from flask import Flask,request,redirect,render_template
app = Flask(__name__)

#logic for the page
@app.route('/',methods=['GET','POST'])
def input():
    #if user submits input, it redirects to api
   if request.method == 'POST':
       #collects the ID from the user
      id = request.form['id']
      #concatenate the  ID with api link
      link = 'https://www.freetogame.com/api/game?id='+id
      #redirect user to link
      return redirect(link)
   #returns the html form to take user input
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
