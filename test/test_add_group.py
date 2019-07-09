# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        old_group=app.group.get_group_list()
        app.group.create(Group("new", "new", "new"))
        new_group=app.group.get_group_list()
        assert len(old_group)+1 == len(new_group)

def test_add_group_empty(app):
        old_group=app.group.get_group_list()
        app.group.create(Group("", "", ""))
        new_group=app.group.get_group_list()
        assert len(old_group)+1 == len(new_group)


