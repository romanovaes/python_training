# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест модификации name"))
        app.group.modify_first_group(Group(name="new name"))


def test_modify_group_header(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест модификации header"))
        app.group.modify_first_group(Group(header="new header"))
