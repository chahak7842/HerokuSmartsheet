import psycopg2
import smartsheet
import json
import sys
import array
import collections

dict1 = {}


s1 = []

sys.setrecursionlimit(10**6)
smartsheet_client = smartsheet.Smartsheet()
sheet = smartsheet_client.Sheets.get_sheet(4067414670370692,include='discussions,attachments,columns,columnType')  
print(sheet)
for x in range(len(sheet.columns)):
    print(sheet.columns[x].type)
    s2 = []
    dict1[sheet.columns[x].title] = sheet.columns[x].type
    print('dict1',dict1[sheet.columns[x].title].value)
   
    typenew = sheet.columns[x].type.value
    print("y is of type:",typenew)
    print('type',type)
    s2.insert(x,sheet.columns[x].title)
    s2.insert(x+1,typenew)
    s1.append(s2)
print(s1)
conn = psycopg2.connect(dbname = "d880or9b563jki", user = "nkdtpihfbhjdjk", password = "f0e1b155c789bb55e992293f71035cc3a9fe6fce5fb3a04e923cd24687b539d4", 
host = "ec2-54-204-28-187.compute-1.amazonaws.com", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

#cur.execute("CREATE TABLE Case (SrNo VARCHAR. PRIMARY KEY,CaseNumber  VARCHAR,Status VARCHAR);")
cur.execute("SELECT * from student;")
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
 
