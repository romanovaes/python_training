# -*- coding: utf-8 -*-
from sys import maxsize
from model.group import Group

def test_add_group(app):
        old_group=app.group.get_group_list()
        group=Group("new", "new", "new")
        app.group.create(group)
        new_group=app.group.get_group_list()
        assert len(old_group)+1 == len(new_group)
        old_group.append(group)
        sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)


def test_add_group_empty(app):
        old_group=app.group.get_group_list()
        group=Group("", "", "")
        app.group.create(group)
        new_group=app.group.get_group_list()
        assert len(old_group)+1 == len(new_group)
        old_group.append(group)
        sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)



