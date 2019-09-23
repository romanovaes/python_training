import random

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

list = []

try:
   l=db.get_group_list_on_id(4)
   cursor = connection.cursor()
   cursor.execute("select group_id from address_in_groups")
   for row in cursor:
                (group_id) = row
                list.append(group_id)
   id_group = random.choice(list)
   print(l[0])
   print(str(id_group[0]))
finally:
    connection.close()