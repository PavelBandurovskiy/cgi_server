import sqlite3

table_sql = sqlite3.connect('cgi-bin/goods_and_services.db')
cursor = table_sql.cursor()

table_sql.execute("""
        CREATE TABLE IF NOT EXISTS goods (
           product VARCHAR(20) PRIMARY KEY,
           typetov VARCHAR NOT NULL,
           raiting INTEGER NOT NULL,
           price INTEGER NOT NULL

);
""")
# lastName VARCHAR(40) NOT NULL,
# fathersName VARCHAR(40) NOT NULL,
table_sql.commit()
table_sql.execute("""
       CREATE TABLE IF NOT EXISTS clients (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       phone INTEGER NOT NULL
       );
""")
table_sql.commit()

table_sql.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product VARCHAR,
            amount INTEGER,
            client_id INTEGER,
            FOREIGN KEY (product) REFERENCES goods(product),
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );
    """)
table_sql.commit()