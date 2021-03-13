import psycopg2
import json
import time

def insert_customer(cur): 
    with open("../json/customers.json", "r") as file:
        customers = json.loads(file.read())
    print("insert customer")
    t1 = time.perf_counter()
    for customer in customers:
        insert = f"INSERT INTO customer VALUES({customer['customer_id']}, {customer['age']}, \'{customer['customer_name']}\')" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")
    return t2-t1 , len(customers)

def insert_products(cur): 
    with open("../json/products.json", "r") as file:
        products = json.loads(file.read())
    print("insert products")
    t1 = time.perf_counter()
    for product in products:
        insert = f"INSERT INTO product VALUES({product['product_id']}, \'{product['product_name']}\')" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")
    return t2-t1 , len(products)

def insert_orders(cur): 
    with open("../json/orders.json", "r") as file:
        orders = json.loads(file.read())
    print("insert orders")
    t1 = time.perf_counter()
    for order in orders:
        insert = f"INSERT INTO orders VALUES({order['order_id']}, {order['customer_id']}, {order['product_id']}, {order['quantity']})" 
        cur.execute(insert)
    t2 = time.perf_counter()
    print(f"time : {t2-t1 : 0.4f}\n")
    return t2-t1 , len(orders)
    

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="thomas")

cur = conn.cursor()


customer_time, customer_len = insert_customer(cur)
product_time, product_len   = insert_products(cur)
order_time   , order_len    = insert_orders(cur)

res_list = []

res_list.append({"table" : "customer", "length" : customer_len, "time" : customer_time})
res_list.append({"table" : "product" , "length" : product_len,  "time" : product_time})
res_list.append({"table" : "orders"  , "length" : order_len,    "time" : order_time})


with open("../json/postgres_insert_result.json", "w") as file:
    json.dump(res_list , file)

conn.commit()

cur.close()
conn.close()