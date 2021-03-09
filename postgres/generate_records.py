
import psycopg2
import json

con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password =  "thomas",
)

cur = con.cursor()

names = [] 

def generate_cusomters:
    with open






cur.close()

con.close()