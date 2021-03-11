import psycopg2
import json
import time



# conn = psycopg2.connect(host="localhost", database="mydb", user="myusr", password="123")
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)
cur = conn.cursor()

queries = (\
    # """SELECT c.customer_name
    # FROM customer as c JOIN orders as o ON
    # c.customer_id = o.customer_id JOIN product as p
    # ON p.product_id = o.product_id WHERE p.product_name = \'p-3\'""",
    """
    UPDATE customer
    SET age = 99999
    where customer_id = 2
    """
    ,
    """
    SELECT c.age
    FROM customer as c
    WHERE customer_id = 2
    """    
)

resultList = []


for query in queries:
    print(f"{query}")
    t1 = time.perf_counter()
    cur.execute(query)
    t2 = time.perf_counter()
    try:
        result = cur.fetchall()
    except:
        result = 0
    res = {"query": query, "time" : t2-t1, "Result" : result}
    resultList.append(res)
    print(f"result : {res}")
    print(f"time : {t2-t1}")
    print("\n")


cur.close()
conn.close()

with open("postgres_result.json", "w+") as file:
    json.dump(resultList,file)
