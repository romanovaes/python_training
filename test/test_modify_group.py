# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
        if len(db.get_group_list())==0:
                app.group.create(Group(name="Тест модификации name"))
        old_groups=db.get_group_list()
        group_old=random.choice(old_groups)
        group=Group(name="name22", header="", footer="")
        group.id=group_old.id
        app.group.modify_group_by_id(group.id, group)
        new_group=db.get_group_list()
        old_groups[old_groups.index(group_old)]=group
        assert sorted(old_groups, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)
        if check_ui:
          assert sorted(map(app.group.clean_gap_from_group, new_group), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



