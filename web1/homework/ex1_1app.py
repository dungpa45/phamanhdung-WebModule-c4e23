from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome "

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    h = height/100
    bmi = weight/(h*h)
    titles = [
        "Ban qua gay",
        "Ban hoi gay ",
        "Ban hoi bi chuan day",
        "Ban hoi beo",
        "Ban qua beo"
    ]
    print("BMI cua ban la:", bmi)
    if bmi < 16:
        return render_template("bmi.html", bmi_index=bmi, content=titles[0])
    elif 16 <= bmi < 18.5:
        return render_template("bmi.html", bmi_index=bmi, content=titles[1])
    elif 18.5 <= bmi < 25:
        return render_template("bmi.html", bmi_index=bmi, content=titles[2])
    elif 255 <= bmi < 30:
        return render_template("bmi.html", bmi_index=bmi, content=titles[3])
    else:
        return render_template("bmi.html", bmi_index=bmi, content=titles[4])

    # return render_template("bmi.html", bmi_index=bmi)


if __name__ == "__main__":
    app.run(debug=True)
