from flask import Flask, request ,render_template, session, redirect ,url_for
import mlab
from models.user import User
from models.movie import Movie

mlab.connect()

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertyuiop"

@app.route("/profile")
def profile():
    if "token" in session:
        username = session["token"]
        user = User.objects(username=username).first()
        movies = Movie.objects(user=user)
        # for m in movies:
        #     print(m.title)
        return render_template("profile.html",movie_list=movies)
    else:
        return "Ko dc vao"


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        u = form["username"]
        p = form["password"]
        found_user = User.objects(username=u).first()        

        if found_user is None: 
            return "No such users"
        elif found_user.password!=p:
            return "Wrong Password"
        else:
            session["token"] = u
            return "ok"

        return "User logging in"

@app.route("/logout")
def logout():
    del session["token"]
    return redirect(url_for("login"))

@app.route("/add_movie", methods=["GET","POST"])
def add_movie():
    if "token" not in session:
        return redirect("/login")
    if request.method == "GET":
        return render_template("add_movie.html")
    elif request.method =="POST":
        form = request.form
        title = form["title"]
        image = form["image"]
        year = form["year"]
        username = session["token"]
        user = User.objects(username=username).first()
        new_movie = Movie(title=title,image=image,year=year,user=user)
        new_movie.save()
        return "OKE"


if __name__ == '__main__':
  app.run(debug=True)
