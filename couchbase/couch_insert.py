import sys

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase import couchbase_core
from couchbase.n1ql import N1QLRequest
import json
import time

def insert_product(collection):
    with open("../json/products.json", "r") as file:
        products = json.loads(file.read())
    print("insert product")
    t1 = time.perf_counter()
    for product in products:
        result = collection.insert(str(product["product_id"]),product)
    t2 = time.perf_counter()
    print(f"time : {t2-t1}")
    return t2-t1, len(products)

def insert_customer(collection):
    with open("../json/customers.json", "r") as file:
        customers = json.loads(file.read())
    print("insert customer")
    t1 = time.perf_counter()
    for customer in customers:
        result = collection.insert(str(customer["customer_id"]),customer)
    t2 = time.perf_counter()
    print(f"time : {t2-t1}")
    return t2-t1, len(customers)
    

def insert_orders(collection):
    with open("../json/ordersCouch.json", "r") as file:
        orders = json.loads(file.read())
    t1 = time.perf_counter()
    for order in orders:
        result = collection.insert(str(order["order_id"]),order)
    t2 = time.perf_counter()
    print(f"time : {t2-t1}")
    return t2-t1, len(orders)

cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))

orders_bkt = cluster.bucket("orders")
customer_bkt = cluster.bucket("customer")
product_bkt = cluster.bucket("product")

# orders_coll = orders_bkt.default_collection()
# customer_coll = customer_bkt.default_collection()
# product_coll = product_bkt.default_collection()

# insert_product(product_bkt)
# insert_customer(customer_bkt)
# insert_order(orders_bkt)

customer_time, customer_len = insert_customer(customer_bkt)
product_time , product_len  = insert_product(product_bkt)
orders_time   , orders_len    = insert_orders(orders_bkt)


res_list = []

res_list.append({"table" : "customer", "length" : customer_len, "time" : customer_time})
res_list.append({"table" : "product" , "length" : product_len, "time" : product_time})
res_list.append({"table" : "orders"  , "length" : orders_len,   "time" : orders_time})


with open("../json/couchbase_insert_result.json", "w") as file:
    json.dump(res_list, file)
