import psycopg2

# conn = psycopg2.connect(host="localhost", database="mydb", user="myusr", password="123")
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)
cur = conn.cursor()


# cur.execute("DELETE FROM orders WHERE order_id IS NOT NULL")
# cur.execute("DELETE FROM customer WHERE customer_id IS NOT NULL")
# cur.execute("DELETE FROM product WHERE product_id IS NOT NULL")

# cur.execute("TRUNCATE orders, product, customer")
# cur.execute("DELETE FROM customer WHERE customer_id IS NOT NULL")
# cur.execute("DELETE FROM product WHERE product_id IS NOT NULL")

# cur.execute("Select * from orders")

# print(cur.fetchall())

conn.commit()

cur.close()
conn.close()