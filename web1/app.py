from flask import Flask,render_template

app = Flask(__name__)

# func binding
@app.route("/") #home page
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello C4E,ahihi"

@app.route("/me")
def me():
    return "Pham Anh Dung, Handsome"

@app.route("/hi/<name>")
def hi_(name):
    return "Hi :) "+name+" handsome too"

@app.route("/add/<int:a>/<int:b>") #dinh nghia ngay
def tong(a,b):
    # s = int(a)+int(b)
    s = a+b
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles =[
        "Troi nang to vai",
        "Troi mua to vl",
        "Troi bao to vkl",
    ]

    contents = [
        "Toi di tan gai",
        "Toi di chu mua",
        "Toi di quay",
    ]

    t = titles[index] 
    c = contents[index]
    return render_template("post.html",title=t,content=c)

@app.route("/movie")
def movie():

    return render_template("movie.html", name="Batman", image="https://media.comicbook.com/2018/06/batman-ben-affleck-rumor-matt-reeves-movie-1113820-1280x0.jpeg")


@app.route("/movies")
def movies():
    # movie_title = [
    #     "Batman",
    #     "Superman",
    #     "Wonder women",
    #     "Flash"
    # ]
    movie_list = [
        {
            "title":"Batman",
            "image": "https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png"
        },
        {
            "title":"Superman",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/SupermanRoss.png/250px-SupermanRoss.png"
        },
        {
            "title":"Wonder women",
            "image": "http://www.costumepartyworld.com/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/w/o/wonder-woman-deluxe-cosplay-costume.jpg"
        },
    ]

    return render_template("movies.html",movies=movie_list)



if __name__ == "__main__":
    app.run(debug=True)

