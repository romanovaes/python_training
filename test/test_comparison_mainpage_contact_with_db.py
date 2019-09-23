# -*- coding: utf-8 -*-
from model.addContact import ContactAdd
import re

def test_comparison_mainpage_contact_with_db(app, db, check_ui):
    contacts_from_home_page=sorted(app.contact.get_contact_list(), key=ContactAdd.id_or_max)
    contacts_from_db=sorted(db.get_contact_list(), key=ContactAdd.id_or_max)
    assert len(contacts_from_home_page)==len(contacts_from_db)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
        assert contacts_from_home_page[i].all_email_from_home_page == merge_email_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phone_like_on_home_page(contacts_from_db[i])


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

def clear(s):
  return re.sub("[() -]", "", s)


def merge_phone_like_on_home_page(contact):
      return "\n".join(filter(lambda x: x!= "",
                              (map(lambda x:clear(x),
                                   filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2])))))
