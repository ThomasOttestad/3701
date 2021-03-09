import sys

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase import couchbase_core
from couchbase.n1ql import N1QLRequest
# from couchbase.n1ql import N1QLQuery

 


# cluster = Cluster.connect("127.0.0.1", ClusterOptions(PasswordAuthenticator("thomas", "thomas")))
# bucket = cluster.bucket("travel-sample")
# collection = bucket.default_collection()

# get a reference to our cluster
cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('thomas', 'thomas')))

bucket = cluster.bucket("test")


collection = bucket.default_collection()

result = cluster.query(
    "DELETE * FROM test WHERE customer_id > 0")

# print(result)

for row in result:
  print(row)

# for row in bucket.n1ql_query('SELECT * FROM default'):
#     print(row)

# "CREATE INDEX ix_test ON test(customer_id);"

# document = {"id":"2"}

# result = collection.insert("test_id", document)

print(collection)

print("!!!!")
# You can access multiple buckets using the same Cluster object.
# another_bucket = cluster.bucket("beer-sample")

# You can access collections other than the default
# if your version of Couchbase Server supports this feature.
# customer_a = bucket.scope("customer-a")
# widgets = customer_a.collection("widgets")