import pymysql.cursors
from fixture.orm import ORMFixture

connection = pymysql.connect(host="127.0.0.1", db="addressbook", user="root", password="")
db=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
    #cursor=connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
       # print(row)
#finally:
    #connection.close()

try:
   l=db.get_contact_list()
   for item in l:
       print(item)
   print(len(l))
finally:
   pass