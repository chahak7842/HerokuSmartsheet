import psycopg2
import smartsheet
import json


conn = psycopg2.connect(dbname = "d880or9b563jki", user = "nkdtpihfbhjdjk", password = "f0e1b155c789bb55e992293f71035cc3a9fe6fce5fb3a04e923cd24687b539d4", 
host = "ec2-54-204-28-187.compute-1.amazonaws.com", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

#cur.execute("CREATE TABLE student (ID SERIAL PRIMARY KEY,NAME  VARCHAR);")
#cur.execute("INSERT INTO student  (name) VALUES(%s)",("Isha",));
#cur.execute("INSERT INTO student  (name) VALUES(%s)",("Praneetha",));
cur.execute("SELECT * from student;")
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()