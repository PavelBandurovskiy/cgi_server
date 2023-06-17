#!/usr/bin/env python3
import cgi
from sql_creation import table_sql, cursor

cursor.execute('SELECT * FROM goods')
data = cursor.fetchall()

html = ('''
<html>
<body>
<h3>Список товаров</h3>
    <table>
        <tr>
            <th>Название товара/услуги</th>
            <th>Тип</th>
            <th>Рейтинг</th>
            <th>Цена в тугриках</th>
            <th>Удаление записи</th>
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
                    <td>{escaped_row[3]}</td>
                    <td><form action="http://localhost:8000/cgi-bin/del_handler_f.py/" method='post' >
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
    
    <html>
        <head>
        
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task 4. Bandurovskiy</title>
            <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
            
            
            <h1>Добавление товара/услуги в БД</h1>
        
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
            
        </head>
        <body>
        
        <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
        <a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a>
        <br><br>
        
          <form action="http://localhost:8000/cgi-bin/first_page_handler.py/" method="POST">
          
            <fieldset>
            
                    <p><label for="tname">Название товара     </label><input type="text" name="tname"></p>
                    <p><label for="type">Выбери тип     </label>
                    <div>
                      <input type="radio" id="tovar" name="type" value="tovar">
                      <label for="tovar">Товар</label>
                    </div>
    
                    <div>
                      <input type="radio" id="yslyga" name="type" value="yslyga">
                      <label for="yslyga">Услуга</label>
                    </div>
                    <p><label for="raiting">Рейтинг     </label><input type="number" name="raiting"></p>
                    <p><label for="price">Цена в тугриках     </label><input type="number" name="price"></p>
            </fieldset>
            <p><input type="submit" class="btn" value="Добавить"></p>
    
          </form>
        </body>
    </html>
    """
)
print(html)