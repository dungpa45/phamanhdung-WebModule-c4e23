from flask import Flask, render_template, request
import mlab
from movie import Movie
from register import Register
from gmail import GMail, Message
gmail = GMail("dungphamanh45@gmail.com", "dung4597")

mlab.connect()
app = Flask(__name__)

@app.route("/add_movie", methods=["GET","POST"])
def add_movie():
    if request.method=="GET":
        # user request form
        return render_template("add_movie.html")
    elif request.method == "POST":

        form = request.form
        t = form["title"]
        img = form["image"]
        y = form["year"]
        m = Movie(title=t,image=img,year=y)
        m.save()
       

        return "Xac Nhan"
        

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        # user request form
        return render_template("add_user.html")
    elif request.method == "POST":

        form = request.form
        u = form["username"]
        e = form["email"]
        p = form["password"]
        

        exist_user = Register.objects(username=u).first()
        exist_mail = Register.objects(email=e).first()
        if exist_user !=None: 
            return "User already exist!"
        if exist_mail != None:
            return "Email already exist!"
        else:
            r = Register(username=u, email=e, password=p)

            r.save()
            message = Message("Chuc mung ban da dang ky thanh cong vao NGANH",to=e)

            gmail.send(message)
        return "Chuc mung!! Ban da dang ky thanh cong"


if __name__=="__main__":
    app.run(debug=True)
