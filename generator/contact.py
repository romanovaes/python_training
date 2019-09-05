from model.addContact import ContactAdd
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opt, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exite(2)

n=5
f="data/contact.json"


for o, a in opt:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string_for_textarea(prefix, maxlen):
        symbols=string.ascii_letters+string.digits+string.punctuation+" "*10
        return prefix+ "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phone(maxlen):
    symbols=string.digits+"-"+"+"+"("+")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_month():
    return random.choice(["January", "February", "March","April","May","June","July","August","September","October","November","December"])

testdata=[ContactAdd(firstname="", middlename="", lastname="")]+[
        ContactAdd(firstname=random_string_for_textarea("name", 5), middlename=random_string_for_textarea("", 5),
                   lastname=random_string_for_textarea("lastname", 5), nickname=random_string_for_textarea("", 5), title=random_string_for_textarea("", 5),
                   company=random_string_for_textarea("", 5), address=random_string_for_textarea("", 5), home=random_string_for_phone(9),
                   mobile=random_string_for_phone(8), work=random_string_for_phone(8), fax=random_string_for_phone(5),
                   email=random_string_for_textarea("email", 5), email2=random_string_for_textarea("email", 5),
                   email3=random_string_for_textarea("email", 5), homepage=random_string_for_textarea("email", 5),
                   bday=str(random.randint(1,31)), bmonth=random_month(), byear=str(random.randint(1900,2030)), aday=str(random.randint(1,31)),
                   amonth=random_month(), ayear=str(random.randint(1900,2030)),address2=random_string_for_textarea("", 5),
                   phone2=random_string_for_phone(9), notes=random_string_for_textarea("", 5)
            )
        for i in range(n)]


file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))