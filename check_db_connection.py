import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

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
   l=db.get_contacts_not_in_group(Group(id='4'))
   for item in l:
       print(item)
   print(len(l))
finally:
   pass