# -*- coding: utf-8 -*-
from builtins import *
from model.group import Group

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

def test_add_group(app, db, json_groups, check_ui):
        group=json_groups
        old_group=db.get_group_list()
        app.group.create(group)
        new_group=db.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)
        if check_ui:
            assert sorted(map(app.group.clean_gap_from_group, new_group), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




