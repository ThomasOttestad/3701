import psycopg2




con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)

cur = con.cursor()


cur.execute("select id, name from test")
rows = cur.fetchall()
# print(rows)
for r in rows:
    # print("afdasdf")
    print(f"id {r[0]} name {r[1]}")


cur.close()

con.close()