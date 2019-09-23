import random

from model.addContact import ContactAdd
from model.group import Group



def test_add_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="тест test_add_contact_in_group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(ContactAdd(firstname="новый контакт"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if not (orm.get_contacts_not_in_group(group)):
        app.contact.create(ContactAdd(firstname="новый контакт"))
    contact = random.choice(orm.get_contact_list())
    list_contacts_old = orm.get_contacts_in_group(group)
    while list_contacts_old.count(contact)>0:
        contact = random.choice(orm.get_contact_list())
    app.commonDef.add_contact_in_group(contactIndex=contact.id, groupId=group.id)
    list_contacts_new=orm.get_contacts_in_group(group)
    list_contacts_old.append(contact)
    assert sorted(list_contacts_old, key=ContactAdd.id_or_max) == sorted(list_contacts_new, key=ContactAdd.id_or_max)
