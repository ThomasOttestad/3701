import sys

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase import couchbase_core
from couchbase.n1ql import N1QLRequest
import json


def insert_product(collection):
    with open("products.json", "r") as file:
        products = json.loads(file.read())
    
    for product in products:
        result = collection.insert(str(product["product_id"]),product)
        # print(result)

# INSERT INTO `product` (KEY, VALUE) VALUES ("key1", { "product_id" : "0", "product_name" : "p-0" });


def insert_customer(collection):
    with open("customers.json", "r") as file:
        customers = json.loads(file.read())
    
    for customer in customers:
        result = collection.insert(str(customer["customer_id"]),customer)
        # print(result)

def insert_order(collection):
    with open("ordersCouch.json", "r") as file:
        orders = json.loads(file.read())
    
    for order in orders:
        result = collection.insert(str(order["order_id"]),order)
        # print(result)

cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))

orders_bkt = cluster.bucket("orders")
customer_bkt = cluster.bucket("customer")
product_bkt = cluster.bucket("product")

# DELETE FROM `product`
# WHERE product_id > 0;


# orders_coll = orders_bkt.default_collection()
# customer_coll = customer_bkt.default_collection()
# product_coll = product_bkt.default_collection()

# insert_product(product_bkt)
# insert_customer(customer_bkt)
insert_order(orders_bkt)

# document = {"id":"2"}
# result = collection.insert("test_id", document)