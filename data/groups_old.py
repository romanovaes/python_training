from model.group import Group
import random
import string
from builtins import *


def random_string(prefix, maxlen):
        symbols=string.ascii_letters+string.digits+string.punctuation+" "*10
        return prefix+ "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Group("", "", "")]+[
        Group(name=random_string("name", 7), header=random_string("header", 5), footer=random_string("footer", 5))
        for i in range(2)]