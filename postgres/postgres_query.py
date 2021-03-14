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

queries = (
        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 10000", 1000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 20000", 20000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 20000", 20000, 3),
        ("SELECT * from product WHERE product_id < 100000" ,10000, 4),

        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 2000", 2000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 40000", 40000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 40000", 40000, 3),
        ("SELECT * from product WHERE product_id < 20000" ,20000, 4),     

        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 3000", 3000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 60000", 60000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 60000", 60000, 3),
        ("SELECT * from product WHERE product_id < 30000" ,30000, 4),   

        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 4000", 4000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 80000", 80000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 80000", 80000, 3),
        ("SELECT * from product WHERE product_id < 40000" ,40000, 4), 

        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 5000", 5000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 100000", 100000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 100000", 100000, 3),
        ("SELECT * from product WHERE product_id < 50000" ,50000, 4), 

        ("SELECT c.customer_name FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where o.product_id < 6000", 6000, 1),
        ("UPDATE customer SET age = age + 1 where customer_id < 120000", 120000, 2),
        ("UPDATE customer SET age = age - 1 where customer_id < 120000", 120000, 3),
        ("SELECT * from product WHERE product_id < 60000" ,60000, 4), 


        # ("SELECT * FROM orders AS o JOIN product AS p ON(o.product_id = p.product_id) JOIN customer AS c ON(c.customer_id = o.customer_id) where c.customer_name LIKE \'%-1%\'", 6000, 1),

        # ("SELECT p.product_name FROM product as p where p.product_name LIKE \'%-%\'", 6000, 1),
        # ("SELECT p.product_name FROM product as p where p.product_name LIKE \'%-%\'", 6000, 1),


)



resultList = []

with open("../json/postgres_result.json", "r+") as file:
    resultList = json.loads(file.read())



for query in queries:
    print(f"{query[0]}")
    t1 = time.perf_counter()
    cur.execute(query[0])
    try:
        result = cur.fetchall()
    except:
        result = 0
    conn.commit()
    t2 = time.perf_counter()
    res = {"query": query[0], "size" : query[1], "type" : query[2], "time" : t2-t1}
    resultList.append(res)
    print(f"time : {t2-t1}")
    print("\n")


cur.close()
conn.close()

with open("../json/postgres_result.json", "w+") as file:
    json.dump(resultList,file)
