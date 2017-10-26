#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Person import Person

oseba1 = Person("Marko", "Vauda", "fakemail@fmail.com", "050222444")
oseba2 = Person(first_name="Alojz", last_name="Čevapar", email="fake@4545.com", phone_number="050667722")
oseba3 = Person(first_name="Borko", last_name="Komentator", email="komentiraj@asd.com", phone_number="051113211")

contact_book = [oseba1, oseba2, oseba3]

def list_contacts(contact_book):
    for index, contact in enumerate(contact_book):
        print "First name: " + contact.first_name
        print "Last name: " + contact.last_name
        print "Full name: " + contact.get_full_name()
        print "Email: " + contact.email
        print "Phone number: " + contact.phone_number
        print ""

    if not contact_book:
        print "Your contact book is empty. Try adding a new contact."

def add_contact(contact_book):
    first_name = raw_input("Please enter contact's first name: ")
    last_name = raw_input("Please enter contact's last name: ")
    email = raw_input("Please enter contact's email address: ")
    phone_number = raw_input("Please enter contact's phone number: ")

    new_contact = Person(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number)
    contact_book.append(new_contact)

    print ""
    print new_contact.get_full_name()+ " was added to your contact book."

def edit_contact(contact_book):
    print "Select the number of the contact you would like to edit: "

    for index, contact in enumerate(contact_book):
        print str(index) + "| " + contact.get_full_name()

    contact_id = raw_input("Which contact would you like to edit? Enter the number next to the contact: ")
    id_transform = contact_book[int(contact_id)]

    updated_name = raw_input("Please enter a new first name for %s: " % id_transform.get_full_name())
    id_transform.first_name = updated_name
    print "First name updated."
    print ""

    updated_lname = raw_input("Please enter a new last name for %s: " % id_transform.get_full_name())
    id_transform.last_name = updated_lname
    print "Last name updated."
    print ""

    updated_email = raw_input("Please enter a new email address for %s: " % id_transform.get_full_name())
    id_transform.email = updated_email
    print "Email updated."
    print ""

    updated_number = raw_input("Please enter a new email address for %s: " % id_transform.get_full_name())
    id_transform.phone_number = updated_number
    print "Phone number updated."
    print ""


def delete_contact(contact_book):
    print "Select the number of the contact you'd like to delete:"

    for index, contact in enumerate(contact_book):
        print str(index) + "| " + contact.get_full_name()

    print ""
    contact_id = raw_input("Which contact would you like to delete? Enter the number next to the contact: ")
    id_transform = contact_book[int(contact_id)]

    contact_book.remove(id_transform)
    print ""
    print "Contact was removed from your contact book."

print "Welcome to your contact book"

while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your contacts"
        print "b) Add a new contact"
        print "c) Edit a contact"
        print "d) Delete a contact"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_contacts(contact_book)
        elif selection.lower() == "b":
            add_contact(contact_book)
        elif selection.lower() == "c":
            edit_contact(contact_book)
        elif selection.lower() == "d":
            delete_contact(contact_book)
        elif selection.lower() == "e":
            print "Thank you for using contact book. Bye!"
            break
        else:
            print "You didn't select a valid option."
            continue