#!/usr/bin/env python3
import cgi
from sql_creation import table_sql, cursor

form = cgi.FieldStorage()

cursor.execute('SELECT product FROM goods')
data_tov = cursor.fetchall()

cursor.execute('SELECT name FROM clients')
data_cl = cursor.fetchall()

print("Content-type: text/html")
html ="""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task 4. Bandurovskiy</title>
            <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
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
          <h1>Добаление заказа в БД</h1>
           <a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a>
           <a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a>
           <br><br>
          <form action="http://localhost:8000/cgi-bin/third_page_handler.py/" method="POST">
            <fieldset>
                    <p> <label for="tname">Выберите товар или услугу</label>
                     <select id="tname" name="tname">
"""

for prod in data_tov:
    html += f"""
        <option value="{str(prod[0])}">{str(prod[0])}</option>
    """
html += """
    </select></p>
    <p><label for="amount">Количество     </label><input type="number" name="amount"></p>
    <p><label for="name">Выберите клиента</label>
        <select id="name" name="name">
        
    
"""

for cl in data_cl:
    html += f"""
        <option value="{str(cl[0])}">{str(cl[0])}</option>
    """

cursor.execute('SELECT * FROM orders')
data = cursor.fetchall()

html += """
    </select>
    </p>
</fieldset>
<p><input type="submit" class="btn" value="Добавить заказик"></p>
</form>

"""
html += """
<h3>Список заказов</h3>
    <table>
        <tr>
            <th>ID заказа</th>
            <th>Продукт/товар</th>
            <th>Количество</th>
            <th>ID клиента</th>
            <th>Удаление заказа</th>
        </tr>
"""

for row in data:
    escaped_row = [str(cell).replace("<", "&lt;").replace(">", "&gt;") for cell in row]
    html += f"""
                <tr>
                    <td>{escaped_row[0]}</td>
                    <td>{escaped_row[1]}</td>
                    <td>{escaped_row[2]}</td>
                    <td>{escaped_row[3]}</td>
                    
                    
                    <td><form action="http://localhost:8000/cgi-bin/del_handler.py/" method='post' >
                        <input type='hidden' name='id' value='{escaped_row[0]}'>
                        <input type='submit' value='Удалить'></form></td>
                    
                </tr>
    """
html += """
    </body>
    </html>
"""
print(html)
