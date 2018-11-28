from flask import Flask ,render_template ,request
from bike import Bike
import mlab

mlab.connect()
app = Flask(__name__)

@app.route("/add_bike", methods=["POST","GET"])
def add_bike():
    if request.method=="GET":
        return render_template("add_bike.html")
    elif request.method=="POST":
        form = request.form
        m = form["model"]
        f = form["fee"]
        i = form["image"]
        y = form["year"]
        b = Bike(model=m,fee=f,image=i,year=y)
        b.save()
    return "Xac nhan"





if __name__ == "__main__":
    app.run(debug=True)
