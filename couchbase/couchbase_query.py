import sys

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase import couchbase_core
from couchbase.n1ql import N1QLRequest
# from couchbase.n1ql import N1QLQuery
import time
import json


queries = \
    (


        ("SELECT customer.customer_name FROM orders where product.product_id < 1000", 1000, 1 ) ,
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 20000", 20000 , 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 20000", 20000,  3),
        ("SELECT product.* from product WHERE product_id < 10000", 10000, 4),

        ("SELECT customer.customer_name FROM orders where product.product_id < 2000", 2000  ,1),
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 40000", 40000, 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 40000", 40000, 3),
        ("SELECT product.* from product WHERE product_id < 20000", 20000, 4),

        ("SELECT customer.customer_name FROM orders where product.product_id < 3000", 3000  ,1),
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 60000", 60000, 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 60000", 60000, 3),
        ("SELECT product.* from product WHERE product_id < 30000", 30000, 4),

        ("SELECT customer.customer_name FROM orders where product.product_id < 4000", 4000 ,1),
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 80000", 80000, 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 80000", 80000, 3),
        ("SELECT product.* from product WHERE product_id < 40000", 40000, 4),

        ("SELECT customer.customer_name FROM orders where product.product_id < 5000", 5000 ,1),
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 100000", 100000, 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 100000", 100000, 3),
        ("SELECT product.* from product WHERE product_id < 50000", 50000, 4),

        ("SELECT customer.customer_name FROM orders where product.product_id < 6000", 6000 ,1) ,
        ("UPDATE customer SET customer.age = customer.age + 1 where customer.customer_id < 120000", 120000, 2),
        ("UPDATE customer SET customer.age = customer.age - 1 where customer.customer_id < 120000", 120000, 3),
        ("SELECT product.* from product WHERE product_id < 60000", 60000, 4),


        # ("SELECT customer.customer_name FROM customer where CONTAINS(customer.customer_name, \"-\")", 6000 ,1)
        # ("SELECT product.* FROM product where CONTAINS(product.product_name, \"-1\")", 6000 ,1),
        # ("SELECT product.product_name FROM product where CONTAINS(product.product_name, \"-\")", 6000 ,1),


        # ("SELECT orders.product_name FROM orders where CONTAINS(product.product_name, \"-\")", 6000 ,1)



        # ("SELECT product_name FROM product where product_id = 0 or \"p-0\" in product.product_name;", 6000 , 1)

        # ("CREATE index product_idx ON product(product_name)", 6000 ,1)
        # ("SELECT product_name FROM product WHERE product_name = \"p-12\"", 6000 ,1)
        
    
    )


# get a reference to our cluster
cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))


resultList = [] 
with open("../json/couch_result.json", "r") as file:
    resultList = json.loads(file.read())

# print(resultList)

for query in queries:
    result = cluster.query(query[0], QueryOptions(metrics = True))
    exec_time = result.metrics['executionTime']
    res = {"query": query[0], "size" : query[1], "type" : query[2], "time" : exec_time}
    resultList.append(res)
    print(res)
    print("\n")




with open("../json/couch_result.json", "w+") as file:
    json.dump(resultList,file)