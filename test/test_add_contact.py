# -*- coding: utf-8 -*-
from model.addContact import ContactAdd

def test_add_contact(app):
    old_contact=app.contact.get_contact_list()
    contact=ContactAdd("Bdftyj", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn")
    app.contact.create(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact=app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=ContactAdd.id_or_max)==sorted(new_contact, key=ContactAdd.id_or_max)

