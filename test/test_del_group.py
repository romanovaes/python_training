# -*- coding: utf-8 -*-
from builtins import len
import  random
from model.group import Group

def test_delete_some_group(app, db, check_ui):
        if len(db.get_group_list())==0:
                app.group.create(Group(name="Тест удаления"))
        old_group=db.get_group_list()
        group=random.choice(old_group)
        app.group.delete_group_by_id(group.id)
        new_group=db.get_group_list()
        assert len(old_group)-1 == len(new_group)
        old_group.remove(group)
        assert old_group==new_group
        if check_ui:
          assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


