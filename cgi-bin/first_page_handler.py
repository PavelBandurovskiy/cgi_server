#!/usr/bin/env python3
import cgi, sqlite3, os
from sql_creation import table_sql, cursor

form = cgi.FieldStorage()

tname = (form.getfirst("tname", ""))
typetov = (form.getfirst("type", ""))
raiting = (form.getfirst("raiting", ""))
price = (form.getfirst("price", ""))


try:
    cursor.executemany("INSERT INTO goods(product, typetov, raiting, price) VALUES(?, ?, ?, ?)", [(str(tname), str(typetov), int(raiting), int(price))])
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
    <h1>Товар успешно добавлен в БД</h1>
    <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
    <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
    <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказ</a>
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
        <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить дядьку</a>
        <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
        </body>
        </html>
        """
    )

