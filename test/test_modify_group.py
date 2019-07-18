# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_modify_group_name(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест модификации name"))
        old_group=app.group.get_group_list()
        index=randrange(len(old_group))
        group=Group(name="new name1")
        group.id=old_group[index].id
        app.group.modify_group_by_index(index, group)
        new_group=app.group.get_group_list()
        assert len(old_group) == len(new_group)
        old_group[index]=group
        sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)


#def test_modify_group_header(app):
        #if app.group.count()==0:
               # app.group.create(Group(name="Тест модификации header"))
       # old_group=app.group.get_group_list()
       # app.group.modify_first_group(Group(header="new header"))
       # new_group=app.group.get_group_list()
       # assert len(old_group) == len(new_group)
