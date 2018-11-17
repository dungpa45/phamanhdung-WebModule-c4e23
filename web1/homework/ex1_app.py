from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome "

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height/100
    bmi = weight/(h*h)

    print("BMI cua ban la:", bmi)
    if bmi < 16:
        return "BMI la: "+str(bmi)+" Ban qua gay"
    elif 16 <= bmi < 18.5:
        return "BMI la: "+str(bmi)+" Ban hoi gay"
    elif 18.5 <= bmi < 25:
        return "BMI la: "+str(bmi)+" Ban hoi bi chuan day"
    elif 255 <= bmi < 30:
        return "BMI la: "+str(bmi)+" Ban hoi beo"
    else:
        return "BMI la: "+str(bmi)+" Ban qua beo" 


if __name__ == "__main__":
    app.run(debug=True)
