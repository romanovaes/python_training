# -*- coding: utf-8 -*-
import random
from random import randrange
from model.addContact import ContactAdd

def test_delete_contact(app, db, check_ui):
        if len(db.get_contact_list())==0:
                app.contact.create(ContactAdd(firstname="Удаление контакта"))
        old_contact=db.get_contact_list()
        contact=random.choice(old_contact)
        app.contact.delete_contact_by_index(int(contact.id))
        new_contact=db.get_contact_list()
        old_contact.remove(contact)
        assert sorted(old_contact, key=ContactAdd.id_or_max) == sorted(new_contact, key=ContactAdd.id_or_max)
        if check_ui:
                assert sorted(map(app.contact.clean_gap_from_contact, old_contact), key=ContactAdd.id_or_max) == sorted(
                        app.contact.get_contact_list(), key=ContactAdd.id_or_max)
