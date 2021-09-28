from flask import Flask, render_template, request
import joblib
import sklearn
import mysql.connector


app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html", data="CHECK YOUR CONDITION")

@app.route("/check", methods = ['POST'])
def check():
    s = []
    name = request.form['name']
    phone = request.form['phone']
    s1 = request.form['s1']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0) 
    s1 = request.form['s2']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s3']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s4']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s5']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s6']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s7']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s8']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s9']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s10']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s11']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s12']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s13']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s14']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s15']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s16']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s17']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s18']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s19']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    s1 = request.form['s20']
    if (s1 == 'y'):
        s.append(1)
    else:
        s.append(0)
    model = joblib.load('BestModel.sav')
    res = model.predict([s])[0]
    if (res == 0):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="covid19"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO negativecases (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        mycursor.execute(sql, val)
        mydb.commit()
        data = "Negative"
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="covid19"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO positivecases (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        mycursor.execute(sql, val)
        mydb.commit()
        data = "Positive"



    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)