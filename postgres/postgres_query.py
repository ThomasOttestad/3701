import psycopg2
import json
import time



conn = psycopg2.connect(host="localhost", database="mydb", user="myusr", password="123")
cur = conn.cursor()

commands = (\
    "SELECT c.customer_name             \n" \
    "FROM customer as c                 \n" \
    "JOIN order_details as o            \n" \
    "ON c.customer_id = o.customer_id   \n" \
    "JOIN product as p                  \n" \
    "ON p.product_id = o.product_id     \n" \
    "WHERE p.product_name = \'p-3\'",


    "SELECT * from customer"
)

for com in commands:
    print(f"{com}")
    t1 = time.perf_counter()
    cur.execute(com)
    t2 = time.perf_counter()
    print(f"result : {cur.fetchall()}")
    print(f"time : {t2-t1}")
    print("\n")

cur.close()
conn.close()