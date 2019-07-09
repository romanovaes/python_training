# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
        if app.group.count()==0:
                app.group.create(Group(name="Тест удаления"))
        old_group=app.group.get_group_list()
        app.group.delete_first_group()
        new_group=app.group.get_group_list()
        assert len(old_group)-1 == len(new_group)


