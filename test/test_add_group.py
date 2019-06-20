# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.session.login("admin", "secret")
        app.group.create(Group("new", "new", "new"))
        app.session.logout()

def test_add_group_empty(app):
        app.session.login("admin", "secret")
        app.group.create(Group("", "", ""))
        app.session.logout()

