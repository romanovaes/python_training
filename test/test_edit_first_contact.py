# -*- coding: utf-8 -*-
from model.addContact import ContactAdd

def test_edit_first_contact(app):
    if app.contact.count()==0:
                app.contact.create(ContactAdd("Контакт для теста", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn"))
    old_contact=app.contact.get_contact_list()
    contact=ContactAdd("Редактирование", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn")
    contact.id=old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact=app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0]=contact
    assert sorted(old_contact, key=ContactAdd.id_or_max)==sorted(new_contact, key=ContactAdd.id_or_max)
