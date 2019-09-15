# -*- coding: utf-8 -*-
from builtins import len
from random import randrange
from model.group import Group

def test_delete_some_group(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест удаления"))
        old_group=app.group.get_group_list()
        index=randrange(len(old_group))
        app.group.delete_group_by_index(index)
        new_group=app.group.get_group_list()
        assert len(old_group)-1 == len(new_group)
        old_group[index:index+1]=[]
        assert old_group==new_group

