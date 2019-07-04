# -*- coding: utf-8 -*-
from model.addContact import ContactAdd

def test_delete_first_contact(app):
        if app.contact.count()==0:
                app.contact.create(ContactAdd(firstname="Удаление контакта"))
        app.contact.delete_first_contact()
