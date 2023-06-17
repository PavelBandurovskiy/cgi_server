#!/usr/bin/env python3
import cgi, sqlite3, os
from sql_creation import table_sql, cursor

form = cgi.FieldStorage()
fio = (form.getfirst("name", ""))
# name, last_name, fathers_name = fio.split()
num = (form.getfirst("number", ""))
# birth = (form.getfirst("birth", ""))

# str(last_name), str(fathers_name),
try:
    cursor.executemany("INSERT INTO clients(name, phone) VALUES(?, ?)", [(str(fio),  int(num))])
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
    <h1>Клиент успешно добавлен в БД</h1>
    <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
    <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
    <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
    </body>
    </html>
    """)

except ValueError:
    print("Content-type: text/html")
    print(
        """
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
        """
    )

