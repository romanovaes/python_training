# -*- coding: utf-8 -*-
from random import randrange
from model.addContact import ContactAdd
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list())==0:
                app.contact.create(ContactAdd("Контакт для теста", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn"))
    old_contact=db.get_contact_list()
    contact = ContactAdd("Редактирование", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn")
    contact_old=random.choice(old_contact)
    contact.id=contact_old.id
    app.contact.edit_contact_by_index(contact, int(contact.id))
    new_contact=db.get_contact_list()
    old_contact[old_contact.index(contact_old)] = contact
    assert sorted(old_contact, key=ContactAdd.id_or_max) == sorted(new_contact, key=ContactAdd.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean_gap_from_contact, old_contact), key=ContactAdd.id_or_max) == sorted(
            app.contact.get_contact_list(), key=ContactAdd.id_or_max)
