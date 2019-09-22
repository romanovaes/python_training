import random

from model.addContact import ContactAdd
from model.group import Group



def test_add_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Тест удаления"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(ContactAdd(firstname="Удаление контакта"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    list_contacts_old = orm.get_contacts_in_group(group)
    app.commonDef.add_contact_in_group(contactIndex=contact.id, groupId=group.id)
    list_contacts_new=orm.get_contacts_in_group(group)
    list_contacts_old.append(contact)
    assert sorted(list_contacts_old, key=ContactAdd.id_or_max) == sorted(list_contacts_new, key=ContactAdd.id_or_max)
