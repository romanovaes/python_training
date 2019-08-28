# -*- coding: utf-8 -*-
from model.addContact import ContactAdd
import pytest
import random
import string

def random_string_for_textarea(prefix, maxlen):
        symbols=string.ascii_letters+string.digits+string.punctuation+" "*10
        return prefix+ "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phone(maxlen):
    symbols=string.digits+"-"+"+"+"("+")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_month():
    return random.choice(["January", "February", "March","April","May","June","July","August","September","October","November","December"])

testdata=[ContactAdd(firstname="", middlename="", lastname="")]+[
        ContactAdd(firstname=random_string_for_textarea("name", 5), middlename=random_string_for_textarea("", 5),
                   lastname=random_string_for_textarea("lastname", 5), nickname=random_string_for_textarea("", 5), title=random_string_for_textarea("", 5),
                   company=random_string_for_textarea("", 5), address=random_string_for_textarea("", 5), home=random_string_for_phone(9),
                   mobile=random_string_for_phone(8), work=random_string_for_phone(8), fax=random_string_for_phone(5),
                   email=random_string_for_textarea("email", 5), email2=random_string_for_textarea("email", 5),
                   email3=random_string_for_textarea("email", 5), homepage=random_string_for_textarea("email", 5),
                   bday=str(random.randint(1,31)), bmonth=random_month(), byear=str(random.randint(1900,2030)), aday=str(random.randint(1,31)),
                   amonth=random_month(), ayear=str(random.randint(1900,2030)),address2=random_string_for_textarea("", 5),
                   phone2=random_string_for_phone(9), notes=random_string_for_textarea("", 5)
            )
        for i in range(2)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact=app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact=app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=ContactAdd.id_or_max)==sorted(new_contact, key=ContactAdd.id_or_max)

