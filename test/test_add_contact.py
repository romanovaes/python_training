# -*- coding: utf-8 -*-
from model.addContact import ContactAdd
import pytest
import random
import string

#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contact):
    contact=json_contact
    old_contact=app.contact.get_contact_list()
    app.contact.create(contact)
    l=app.contact.count()
    assert len(old_contact)+1 == l
    new_contact=app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=ContactAdd.id_or_max)==sorted(new_contact, key=ContactAdd.id_or_max)

