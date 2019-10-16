import pymysql.cursors
from model.group import Group
from model.addContact import ContactAdd
import allure

class DBFixture:

    def __init__(self, host, name, user, password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection=pymysql.connect(host=host, db=name, user=user, password=password, autocommit=True)

    @allure.step('db.get_group_list')
    def get_group_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
            return list

    @allure.step('db.get_contact_list')
    def get_contact_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(ContactAdd(
                    id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work,email=email, email2=email2, email3=email3, phone2=phone2))
        finally:
            cursor.close()
            return list

    def get_group_id_with_contact(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (group_id) = row
                list.append(group_id)
        finally:
            cursor.close()
            return list


    def get_group_on_id(self, id):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where group_id=%s" % id)
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
            return list

    def destroy(self):
        self.connection.close()