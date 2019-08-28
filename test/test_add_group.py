# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
        symbols=string.ascii_letters+string.digits+string.punctuation+" "*10
        return prefix+ "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Group("", "", "")]+[
        Group(name=random_string("name", 7), header=random_string("header", 5), footer=random_string("footer", 5))
        for i in range(2)]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        old_group=app.group.get_group_list()
        app.group.create(group)
        assert len(old_group)+1 == app.group.count()
        new_group=app.group.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key=Group.id_or_max)==sorted(new_group, key=Group.id_or_max)




