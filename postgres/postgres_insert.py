import psycopg2
import json
import time

def insert_customer(cur): 
    with open("customers.json", "r") as file:
        customers = json.loads(file.read())
    print("insert customer")
    t1 = time.perf_counter()
    for customer in customers:
        insert = f"INSERT INTO customer VALUES({customer['customer_id']}, {customer['age']}, \'{customer['customer_name']}\')" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")

def insert_products(cur): 
    with open("products.json", "r") as file:
        products = json.loads(file.read())
    print("insert products")
    t1 = time.perf_counter()
    for product in products:
        insert = f"INSERT INTO product VALUES({product['product_id']}, \'{product['product_name']}\')" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")

def insert_orders(cur): 
    with open("orders.json", "r") as file:
        orders = json.loads(file.read())
    print("insert orders")
    t1 = time.perf_counter()
    for order in orders:
        insert = f"INSERT INTO order_details VALUES({order['order_id']}, {order['customer_id']}, {order['product_id']}, {order['quantity']})" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")


conn = psycopg2.connect(host="localhost", database="mydb", user="myusr", password="123")

cur = conn.cursor()

insert_customer(cur)
insert_products(cur)
insert_orders(cur)

# commands = (\
#     "SELECT c.customer_name             \n" \
#     "FROM customer as c                 \n" \
#     "JOIN order_details as o            \n" \
#     "ON c.customer_id = o.customer_id   \n" \
#     "JOIN product as p                  \n" \
#     "ON p.product_id = o.product_id     \n" \
#     "WHERE p.product_name = \'p-3\'",
#     "SELECT * from customer"
# )

# for com in commands:
#     print(f"{com}")
#     t1 = time.perf_counter()
#     cur.execute(com)
#     t2 = time.perf_counter()
#     # print(f"result : {cur.fetchall()}")
#     print(f"time : {t2-t1 : 0.4f}")
#     print("\n")


# conn.commit()
cur.close()
conn.close()