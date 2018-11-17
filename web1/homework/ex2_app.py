from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome "

@app.route("/user/<username>")
def user(username):
    users = {
        "huy":{
            "name": "Nguyen Quang Huy",
            "age": 29
        },
        "tuan anh":{
            "name": "Huynh Tuan Anh",
            "age": 22
        },
        "dung":{
            "name": "Pham Anh Dung",
            "age": 21
        }
    }
    
    if username in users:
        u = users[username]
        return render_template("user.html",user = u )
    else:
        return "User not found"
    

if __name__ == "__main__":
    app.run(debug=True)
