#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    first_name = ""
    last_name = ""
    email = ""
    phone_number = ""

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_full_name(self):
        return self.first_name + " " + self.last_name