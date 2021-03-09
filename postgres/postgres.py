import psycopg2




con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)

cur = con.cursor()

cur.execute("insert into test (name, id) values (%s, %s)", ('{cec}', 2))
cur.execute("insert into test (name, id) values (%s, %s)", ('{thomas}', 1))



# cur.execute("select id, name from test")
# rows = cur.fetchall()
# print(rows)
# for r in rows:
#     print("afdasdf")
#     print(r)

# print("!!!!!!!!!!!!!!!")
con.commit()


cur.close()

con.close()
