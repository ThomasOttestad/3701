import psycopg2


con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)

cur = con.cursor()

commands = (
    """CREATE TABLE customer(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);""",

"""CREATE TABLE product(
   product_id INT GENERATED ALWAYS AS IDENTITY,
   product_name VARCHAR(255) NOT NULL,
   price INT NOT NULL,
   PRIMARY KEY(product_id)
);""",

"""CREATE TABLE orders(
   order_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT REFERENCES customer(customer_id) NOT NULL,
   product_id INT REFERENCES product(product_id) NOT NULL,
   quantity INT NOT NULL,
   created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
   PRIMARY KEY(order_id)
);""",


)
for com in commands:
    cur.execute(com)


con.commit()


cur.close()

con.close()