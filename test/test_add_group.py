# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.session.login("admin", "secret")
        app.create_group(Group("new", "new", "new"))
        app.session.logout()

def test_add_group_empty(app):
        app.session.login("admin", "secret")
        app.create_group(Group("", "", ""))
        app.session.logout()

