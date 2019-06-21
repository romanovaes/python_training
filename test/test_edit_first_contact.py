# -*- coding: utf-8 -*-
from model.addContact import ContactAdd

def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(ContactAdd("Edit", "Petrov", "Petrov2", "Petr", "title test", "cjmpany222", "Svobod1", "348758937", "234234324", "34534534", "345345345", "dfgdf@dfgdf.er", "dfgdfg@fghfg.er", "dfgdf@dfgd.er", "jhjhj.re", "11", "September", "1990", "11", "March", "2000", "flhrtccx", "Ferabd,2", "ytn"))
    app.session.logout()