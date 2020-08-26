import os
import sqlite3
from flask import Flask , render_template , request , redirect , session
app = Flask(__name__)

app.secret_key = 'sunabaco'

from datetime import datetime

@app.route('/',methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect ('/index')
        else:
            return render_template("register.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect('himawari.db')
        c = conn.cursor()
        c.execute("insert into user values(null,?,?)", (name,password))
        conn.commit()
        conn.close()
        return redirect('/login')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect("/index")
        else:
            return render_template("login.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect('himawari.db')
        c = conn.cursor()
        c.execute("select id from user where name = ? and password = ?", (name, password) )
        user_id = c.fetchone()
        conn.close()
        print(type(user_id))
        if user_id is None:
            return render_template("login.html")
        else:
            session['user_id'] = user_id[0]
            return redirect("/index")

@app.route("/index")
def index():
    if 'user_id' in session :
        user_id = session['user_id']
        conn = sqlite3.connect('himawari.db')
        c = conn.cursor()
        c.execute("select name from user where id = ?", (user_id,))
        user_info = c.fetchone()
#         # user_infoの中身を確認

#         # 課題1の答えはここ del_flagが0のものだけ表示する
#         # 課題2の答えはここ 保存されているtimeも表示する
#         c.execute("select id,time from user where userid = ?  = 0 order by id", (user_id,))
#         for row in c.fetchall():
#             comment_list.append({"id": row[0], "time":row[1]})

        c.close()
        return render_template('index.html')
    else:
        return redirect("/login")


@app.route("/hospital")
def hospital():
    return render_temlate('hospital.html')

@app.route("/where")
def where():
    return render_template('where.html')






if __name__ == "__main__":
    
    app.run(debug=True)