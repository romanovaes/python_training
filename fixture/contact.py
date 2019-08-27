from model.addContact import ContactAdd
from selenium.webdriver.support.ui import Select
import re

class ContactHelper:

    def __init__(self, app):
        self.app=app

    def open_created_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_created_contact()
        self.fill_contact(contact)
        #enter contact
        wd.find_element_by_xpath("/html/body/div/div[4]/form/input[1]").click()
        self.app.open_home_page()
        self.contact_cache=None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        #select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #delete contact
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        #alert delete
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache=None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_home_page()
        #open  contact to edit
        wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img")[index].click()
        self.fill_contact(contact)
        #safe edition to contact
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache=None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact,0)


    def fill_contact(self, contact):
        wd = self.app.wd
        # fill form
        self.change_field_in_contact("firstname", contact.firstname)
        self.change_field_in_contact("middlename", contact.middlename)
        self.change_field_in_contact("lastname", contact.lastname)
        self.change_field_in_contact("nickname", contact.nickname)
        self.change_field_in_contact("title", contact.title)
        self.change_field_in_contact("company", contact.company)
        self.change_field_in_contact("address", contact.address)
        self.change_field_in_contact("home", contact.home)
        self.change_field_in_contact("mobile", contact.mobile)
        self.change_field_in_contact("work", contact.work)
        self.change_field_in_contact("fax", contact.fax)
        self.change_field_in_contact("email", contact.email)
        self.change_field_in_contact("email2", contact.email2)
        self.change_field_in_contact("email3", contact.email3)
        self.change_field_in_contact("homepage", contact.homepage)
        # fill date
        self.change_day_and_month("bday", contact.bday)
        self.change_day_and_month("bmonth", contact.bmonth)
        self.change_field_in_contact("byear", contact.byear)
        self.change_day_and_month("aday", contact.aday)
        self.change_day_and_month("amonth", contact.amonth)
        self.change_field_in_contact("ayear", contact.ayear)
        # fill address and phone
        self.change_field_in_contact("address2", contact.address2)
        self.change_field_in_contact("phone2", contact.phone2)
        self.change_field_in_contact("notes", contact.notes)
        self.change_field_in_contact("homepage", contact.homepage)
        self.change_field_in_contact("homepage", contact.homepage)
        self.change_field_in_contact("homepage", contact.homepage)

    def change_field_in_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

    def change_day_and_month(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def count(self):
         wd = self.app.wd
         self.app.open_home_page()
         return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
           wd = self.app.wd
           self.app.open_home_page()
           self.contact_cache=[]
           for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
              text=element.find_element_by_css_selector("td:nth-child(2)").text
              text1=element.find_element_by_css_selector("td:nth-child(3)").text
              id=element.find_element_by_name("selected[]").get_attribute('value')
              all_phones=element.find_element_by_css_selector("td:nth-child(6)").text
              self.contact_cache.append(ContactAdd(firstname=text1, lastname=text, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        #open  contact to edit
        wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img")[index].click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(0)
        firstname=wd.find_element_by_name("firstname").get_attribute("value")
        lastname=wd.find_element_by_name("lastname").get_attribute("value")
        id=wd.find_element_by_name("id").get_attribute("value")
        homephone=wd.find_element_by_name("home").get_attribute("value")
        workphone=wd.find_element_by_name("work").get_attribute("value")
        mobilephone=wd.find_element_by_name("mobile").get_attribute("value")
        secondphone=wd.find_element_by_name("phone2").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        email=wd.find_element_by_name("email").get_attribute("value")
        email2=wd.find_element_by_name("email2").get_attribute("value")
        email3=wd.find_element_by_name("email3").get_attribute("value")
        return ContactAdd(firstname=firstname,lastname=lastname, id=id,
                       home=homephone,  work=workphone, mobile=mobilephone, phone2=secondphone,
                          address=address, email=email, email2=email2, email3=email3)

    def get_contact_list_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text=wd.find_element_by_id("content").text
        homephone=re.search("H: (.*)", text).group(1)
        workphone=re.search("W: (.*)", text).group(1)
        mobilephone=re.search("M: (.*)", text).group(1)
        secondphone=re.search("P: (.*)", text).group(1)
        return ContactAdd(home=homephone,  work=workphone, mobile=mobilephone, phone2=secondphone)


    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()






