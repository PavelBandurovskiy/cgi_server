#!/usr/bin/env python3

print("Content-type: text/html")
print("""
<html>
        <head>
        
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task 4. Bandurovskiy</title>
            <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
            <h1>Дратути</h1>
            <style>
                a{
                    padding: 8px;
                    margin: 10px;
                    text-decoration: none;
                    background-color: #4CAF50;
                    color: white;
                }
            </style>
        </head>
        <br><br>
        <p><a href="http://localhost:8000/cgi-bin/first_page.py/">Добавить товар</a></p>
        <br>
        <p><a href="http://localhost:8000/cgi-bin/second_page.py/">Добавить клиента</a></p>
        <br>
        <p><a href="http://localhost:8000/cgi-bin/third_page.py/">Добавить заказик</a></p>
""")