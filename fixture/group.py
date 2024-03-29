import allure

from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app=app

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
           wd.find_element_by_link_text("groups").click()

    @allure.step('create_group')
    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache=None

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
       self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #delete group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache=None

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        # select first group
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_group_by_index(self,index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()


    def modify_group_by_index(self, index, new_group_data):
        wd =self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #open modification group
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache=None

    def modify_group_by_id(self, id, new_group_data):
        wd=self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        #open modification group
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache=None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def count(self):
        wd=self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache=None

    def get_group_list(self):
        if self.group_cache is None:
           wd=self.app.wd
           self.open_group_page()
           self.group_cache=[]
           for element in wd.find_elements_by_css_selector('span.group'):
              text=element.text
              id=element.find_element_by_name("selected[]").get_attribute('value')
              self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None


    def clean_gap_from_group(self,group):
        return Group(id=group.id, name=group.name.strip(), header=group.header.strip(), footer=group.footer.strip())