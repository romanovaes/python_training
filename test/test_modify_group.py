# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест модификации name"))
        old_group=app.group.get_group_list()
        app.group.modify_first_group(Group(name="new name"))
        new_group=app.group.get_group_list()
        assert len(old_group) == len(new_group)


def test_modify_group_header(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест модификации header"))
        old_group=app.group.get_group_list()
        app.group.modify_first_group(Group(header="new header"))
        new_group=app.group.get_group_list()
        assert len(old_group) == len(new_group)
