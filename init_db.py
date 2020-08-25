import sqlite3

# service.dbとつなぐ(なければ作られる)
conn = sqlite3.connect('himawari.db')
c = conn.cursor()

# テーブル作成
c.execute("create table user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)")
c.execute("create table health(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, condition TEXT)")
c.execute("create table hosp(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, hospital TEXT)")
c.execute("create table where(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, schedule TEXT)")

# 確定
conn.commit()

# バイバイ
conn.close()