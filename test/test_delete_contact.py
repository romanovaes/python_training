# -*- coding: utf-8 -*-
from random import randrange
from model.addContact import ContactAdd

def test_delete_contact(app):
        if app.contact.count()==0:
                app.contact.create(ContactAdd(firstname="Удаление контакта"))
        old_contact=app.contact.get_contact_list()
        index=randrange(len(old_contact))
        app.contact.delete_contact_by_index(index)
        new_contact=app.contact.get_contact_list()
        assert len(old_contact)-1 == len(new_contact)
        old_contact[index:index+1]=[]
        assert old_contact==new_contact
