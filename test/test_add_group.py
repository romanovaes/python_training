# -*- coding: utf-8 -*-
from model.group import Group

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

def test_add_group(app, data_groups):
        group=data_groups
        old_group=app.group.get_group_list()
        app.group.create(group)
        assert len(old_group)+1 == app.group.count()
        new_group=app.group.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)




