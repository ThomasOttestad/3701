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
        "SELECT customer.customer_name FROM orders WHERE product.product_id = 5",
        "SELECT product.product_name FROM orders WHERE customer.customer_id = 8",
        "SELECT customer.customer_name FROM orders WHERE (product.product_id = 6 OR product.product_id = 3) AND customer.age > 25",
        "SELECT product_name FROM product WHERE product_id > 0",
        "SELECT customer_name FROM customer WHERE customer_id = 1 or customer_id = 3",
    )


# get a reference to our cluster
cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))
resultList = []

for query in queries:
    t1 = time.perf_counter()
    result = cluster.query(query)   
    t2 = time.perf_counter()
    res = {"query": query, "time" : t2-t1, "Result" : result.rows()}
    resultList.append(res)
    print(query)
    for row in result:
        print(row)
    print("\n")

with open("couch_result.json", "w+") as file:
    json.dump(resultList,file)