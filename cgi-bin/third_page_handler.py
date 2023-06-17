#!/usr/bin/env python3
import cgi, sqlite3, os
from sql_creation import table_sql, cursor

form = cgi.FieldStorage()

tname = (form.getfirst("tname", ""))
amount = (form.getfirst("amount", ""))
name = (form.getfirst("name", ""))

cursor.execute(f"SELECT id FROM clients WHERE name = '{name}'")
id_pers = cursor.fetchall()
id_p = id_pers[0][0]

try:
    cursor.executemany("INSERT INTO orders(product, amount, client_id) VALUES(?, ?, ?)", [(str(tname),  int(amount), int(id_p))])
    table_sql.commit()
    print("Content-type: text/html")
    print(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Данные отправлены успешно</title>
    </head>
    <body>
    <h1>Заказик успешно добавлен в БД</h1>
    <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
    <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
    <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
    </body>
    </html>
    """)


except ValueError:
    print("Content-type: text/html")
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Произошла ошибка</title>
        </head>
        <body>
        <h1>Произошла ошибка попробуй еще раз</h1>

        <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
        <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
        <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
        </body>
</html>
""")