from datetime import time

from model.addContact import ContactAdd
from selenium.webdriver.support.ui import Select
import re
from model.group import Group


class ContactGroupHelper:

    def __init__(self, app):
        self.app = app

    def add_contact_in_group(self, contactIndex, groupId):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contactIndex).click()
        wd.find_element_by_css_selector("select[name='to_group']").click()
        wd.find_element_by_css_selector('select[name="to_group"] > option[value="%s"]' % groupId).click()
        wd.find_element_by_name('add').click()


    def remove_contact_in_group(self, contactIndex, groupId):
        wd = self.app.wd
        wd.find_element_by_name('group').click()
        wd.find_element_by_css_selector('select[name="group"] > option[value="%s"]' % groupId).click()
        time.sleep(2)
        wd.find_element_by_css_selector("input[value='%s']" % contactIndex).click()
        wd.find_element_by_name('remove').click()
