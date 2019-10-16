# -*- coding: utf-8 -*-
from model.addContact import ContactAdd
import pytest
import random
import string
from builtins import *
import allure


@allure.step('test_add_contact')
def test_add_contact(app, db, json_contact, check_ui):
    contact=json_contact
    old_contact=db.get_contact_list()
    app.contact.create(contact)
    new_contact=db.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=ContactAdd.id_or_max) == sorted(new_contact, key=ContactAdd.id_or_max)
    if check_ui:
      assert sorted(map(app.contact.clean_gap_from_contact, old_contact), key=ContactAdd.id_or_max)==sorted(
          app.contact.get_contact_list(), key=ContactAdd.id_or_max)

