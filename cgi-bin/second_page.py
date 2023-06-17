#!/usr/bin/env python3
import cgi
from sql_creation import table_sql, cursor

cursor.execute('SELECT * FROM clients')
data = cursor.fetchall()

html = ('''
<html>
<body>
<h3>Список клиентов</h3>
    <table>
        <tr>
            <th>ID</th>
            <th>Имя</th>
            <th>Номер телефона</th>
            <th>Удаление клиента</th>
        </tr>
''')

for row in data:
    # Экранируем данные из базы данных
    escaped_row = [str(cell).replace("<", "&lt;").replace(">", "&gt;") for cell in row]
    html += f"""
                <tr>
                    <td>{escaped_row[0]}</td>
                    <td>{escaped_row[1]}</td>
                    <td>{escaped_row[2]}</td>
                    <td><form action="http://localhost:8000/cgi-bin/del_handler_s.py/" method='post' >
                        <input type='hidden' name='id' value='{escaped_row[0]}'>
                        <input type='submit' value='Удалить'></form></td>
                </tr>
    """

html += '''
    </table>
</body>
</html>
'''


print("Content-type: text/html")
print(
    """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task 4. Bandurovskiy</title>
        </head>
        
          <h1>Добавление клиента в БД</h1>
        
          <title>Список товаров</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        
        .btn{
            background-color: #4CAF50;
            padding: 8px;
            color: white;
        }

        th, td {
            text-align: left;
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
    <body>
    <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
        <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
        <br><br>
    
          <form action="http://localhost:8000/cgi-bin/second_page_handler.py/" method="POST">
            <fieldset>
                    <p><label for="name">ФИО     </label><input type="text" name="name"></p>
                    <p><label for="number">Введи номер телефона     </label><input type="number" name="number"></p>
            </fieldset>
            <p><input type="submit" class="btn" value="Добавить клиента"></p>

          </form>
        </body>
    </html>
    """
)

print(html)