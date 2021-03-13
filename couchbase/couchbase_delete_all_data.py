import sys

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase import couchbase_core
from couchbase.n1ql import N1QLRequest
# from couchbase.n1ql import N1QLQuery

 




# get a reference to our cluster
cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))


# deleteCustomer = cluster.query(
#     "DELETE FROM `customer` where customer_id IS NOT NULL RETURNING *")

deleteCustomer = cluster.query("DELETE FROM orders where order_id IS NOT NULL;")

print(deleteCustomer)

# DELETE FROM `product`
# WHERE product_id > 0;
