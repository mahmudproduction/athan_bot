import sqlite3
import config
import logging
try:
   conn = sqlite3.connect(config.sqldatabase) #За соединение будет отвечать переменная conn.Если файл уже существует, то функция connect осуществит подключение к нему.Путь должен прописоваться от корня. Узнать можно в настройках
   cur = conn.cursor()#После создания объекта соединения с базой данных нужно создать объект cursor
   print("Database connect in utils: Ok")
except Exception as err:
   print(f"Database connect eror in utils:{err}")
# Модуль добавления в базу логирования,  тех кто нажал кнопку старт
def hello(a, b, c, d, f):
   query = (None, a, b, c, d, f)
   cur.execute("INSERT INTO actions VALUES(?, ?, ?, ?, ?, ?);", query )
   conn.commit()
   if not c:
      SOBAKA = "Id:"
   else:
      SOBAKA = "@"  
   logging.info(f"~{b}({SOBAKA}{c or a})~ is {d}")
# Модуль добваления нового пользователя в базу
def add_usr(j,k,m,n,l,p,r,s):
   add_users=(None, j, k, m, n, l, p, r, 1,s)
   cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? );", add_users)
   conn.commit()

# Модуль проверки существования пользователя
def check_user(u_id):

   cur.execute(f"SELECT * FROM users WHERE u_id={u_id} ORDER BY id DESC;")
   check_users = cur.fetchone()
   return check_users


# Мод обнуления настроек пользователя
def user_setting_null(u_id):

   try:
      cur.execute(f"UPDATE users SET status = 0 WHERE u_id={u_id};"  )
      conn.commit()
      answ = "Пользователь обнулился"
   except Exception as err:
      answ = err  
   return answ


   # message.chat.id => a
   # message.from_user.first_name => b
   # message.chat.username => c
   # 'ACTIONS'=> d
   # ath_time.today_epohe=> f
