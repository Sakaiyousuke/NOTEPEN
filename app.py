import os
import sqlite3
from flask import Flask , render_template , request , redirect , session
app = Flask(__name__)

app.secret_key = 'sunabaco'

import datetime

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

@app.route("/logout")
def logout():
    session.pop('user_id',None)
    # ログアウト後はログインページにリダイレクトさせる
    return redirect("/login")

# インデックス

@app.route("/index")
def index():
    if 'user_id' in session :
        user_id=session['user_id']
        conn = sqlite3.connect('himawari.db')
        c = conn.cursor()
        c.execute("select name from user where id = ?", (user_id,))
        user_name = c.fetchone()


        c.close()
        today = datetime.date.today()
        print(today.year,today.month,today.day)
        return render_template('index.html',user_name=user_name,today=today)
    else:
        return redirect("/login")

@app.route('/maru' , methods=["POST"])
def maru_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO health VALUES (null,?,1)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/hospital")

@app.route('/batu' , methods=["POST"])
def batu_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO health VALUES (null,?,2)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/hospital")


# ホスピタル

@app.route("/hospital")
def hospital():
    return render_template('hospital.html')

@app.route('/good' , methods=["POST"])
def good_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO hosp VALUES (null,?,1)", (user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/where")

@app.route('/bad' , methods=["POST"])
def bad_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO hosp VALUES(null,?,2)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/where")


# ウェヤ

@app.route("/where")
def where():
    return render_template('where.html')

@app.route('/shopping' , methods=["POST"])
def shopping_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO hosp VALUES(null,?,1)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")

@app.route('/hobby' , methods=["POST"])
def hobby_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO hosp VALUES(null,?,2)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")

@app.route('/walking' , methods=["POST"])
def walking_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO place VALUES(null,?,3)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")

@app.route('/friend' , methods=["POST"])
def friend_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO place VALUES(null,?,4)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")

@app.route('/trip' , methods=["POST"])
def trip_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO place VALUES(null,?,5)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")

@app.route('/warking' , methods=["POST"])
def warking_task():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO place VALUES(null,?,6)",(user_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/one")
    
@app.route("/one")
def one():
    # if 'user_id' in session: 
    #     user_id=session['user_id']
    #     conn=sqlite3.connect('himawari.db')
    #     c=conn.cursor()
    #     c.execute("select name from user where id = ?", (user_id,))
    #     user_name = c.fetchone()

    #     # c.execute("select comment from bbs where id=?",(comment,))
    #     print(c.execute("select comment from bbs where id=1"))
    #     comment_list=[]
    #     for row in c.fetchall():
    #         comment_list.append({"id":row[0],"comment":[30]})
            
    #     c.close()    
    #     today = datetime.date.today()
    #     print(today.year,today.month,today.day)

        return render_template('one.html')
        # ,user_name=user_name,comment_list=comment_list,today=today)
    # else:
    #     return redirect("/login")

@app.route("/bbs")
def bbs():
    user_id=session['user_id']
    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    c.execute("select name from user where id = ?", (user_id,))
    user_name = c.fetchone()

    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    c.execute("select condition from health where user_id = ?", (user_id,))
    user_condition = c.fetchone()

    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    c.execute("select hospital from hosp where user_id = ?", (user_id,))
    user_hospital = c.fetchone()

    conn = sqlite3.connect('himawari.db')
    c = conn.cursor()
    c.execute("select schedule from place where user_id = ?", (user_id,))
    user_schedule = c.fetchone()


    c.close()
    today = datetime.date.today()
    print(today.year,today.month,today.day)
    print(user_condition)
    print(user_condition[0])
    print(type(user_condition[0]))
    if user_condition[0] == "1":
        user_condition = "元気"
    else:
        user_condition = "元気じゃない"
    
    if user_hospital[0] == "1":
        user_hospital = "病院に行く"
    else:
        user_hospital ="病院に行かない"
    
    if user_schedule[0] == "1":
        user_schedule = "買い物に行く"
    elif user_schedule[0] == "2":
        user_schedule = "趣味"
    elif user_schedule[0] == "3":
        user_schedule = "散歩に行く"
    elif user_schedule [0] == "4":
        user_schedule = "旅行に行く"
    else: 
        user_schedule [0] == 5
        user_schedule = "仕事をする"
    # else:
    #     user_schedule[0] == 6
    #     user_schedule = "家にいます"

    return render_template('bbs.html',user_name = user_name,today=today,user_condition = user_condition,user_hospital=user_hospital,user_schedule=user_schedule)
    
    






if __name__ == "__main__":
    
    app.run(debug=True)