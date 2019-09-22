import random

from model.addContact import ContactAdd
from model.group import Group



def test_remove_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Тест удаления"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactAdd(firstname="Удаление контакта"))
    if len(db.get_group_id_with_contact())==0:
        print("Необходимо выполнить тест добавления контакта в группу")

    id_group=random.choice(db.get_group_id_with_contact())
    group=orm.get_group_list_on_id(str(id_group))
    list_contacts_old = orm.get_contacts_in_group(group)
    contact = random.choice(db.list_contacts_old())
    app.commonDef.remove_contact_in_group(contactIndex=contact.id, groupId=id_group)
    list_contacts_new=orm.get_contacts_in_group(group)
    list_contacts_old.remove(contact)
    assert sorted(list_contacts_old, key=ContactAdd.id_or_max) == sorted(list_contacts_new, key=ContactAdd.id_or_max)
