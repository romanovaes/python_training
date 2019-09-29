import random

from model.addContact import ContactAdd
from model.group import Group



def test_remove_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Удаление контакта"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactAdd(firstname="Удаление контакта"))
    if len(db.get_group_id_with_contact()) == 0:
        group = random.choice(orm.get_group_list())
        contact_add = random.choice(orm.get_contact_list())
        app.commonDef.add_contact_in_group(contactIndex=contact_add.id, groupId=group.id)
        id_group = group.id
    else:
        id_group=random.choice(db.get_group_id_with_contact())[0]
    list_contacts_old = orm.get_contacts_in_group(Group(id=str(id_group)))
    contact = random.choice(list_contacts_old)
    app.commonDef.remove_contact_in_group(contactIndex=contact.id, groupId=id_group)
    list_contacts_new=orm.get_contacts_in_group(Group(id=str(id_group)))
    list_contacts_old.remove(contact)
    assert sorted(list_contacts_old, key=ContactAdd.id_or_max) == sorted(list_contacts_new, key=ContactAdd.id_or_max)
