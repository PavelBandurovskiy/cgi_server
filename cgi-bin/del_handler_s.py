#!/usr/bin/env python3
import cgi, sqlite3, os
from sql_creation import table_sql, cursor

form = cgi.FieldStorage()

id_to_delete = form.getfirst('id')

# cursor.execute(f"SELECT id FROM clients WHERE name = '{name}'")
# id_pers = cursor.fetchall()
# id_p = id_pers[0][0]

try:
    cursor.execute("DELETE FROM clients WHERE id=?", (id_to_delete,))
    table_sql.commit()
    print("Content-type: text/html")
    print(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Данные удалены успешно</title>
    </head>
    <body>
    <h1>Данные удалены успешно</h1>
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