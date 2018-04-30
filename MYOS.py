import hashlib #To encode passwords
import math
import time

system_operate_list = {}
users = []
passwords = {}

def encode_password(password):
    encoded_password = hashlib.md5(password)
    return encoded_password
#use md5 hash algorism to encode password

def create_user():
    username = raw_input("  Username:")
    password1 = raw_input("  Password:")
    password2 = raw_input("  Confirm password:")
    if password1 == password2:
        users.append(username)
        passwords[username] = password1
        system_operate_list["first_enter"] = False
    else:
        print "Please try again later..."
    return
def login():
    print "Please log in by entering username:"
    username = raw_input("  Username:")
    user_exist = False
    for i in xrange(len(users)):
        if users[i] == username:
            user_exist = True
            break
    if user_exist == True:
        password = raw_input("  Password:")
        if password == passwords[username]:
            system_operate_list["login"] = True
            print "Welcome",username
            main(username)
        else:
            print "Invalid password..."
    else:
        print "User does not exist..."
    return
def print_help():
    print "Currently available commands:"
    print '''
    help --- get help.
    lst usr --- list saved users.
    new user --- create a new user.
    '''
    return
def main(username):
    command = raw_input(">>>")
    if command == "help":
        print_help()
        main(username)
    else:
        print "Unknown command..."
        main(username)
    return
def start_up():
    if system_operate_list["first_enter"] == True:
        print "Please create a new user:"
        create_user()
    else:
        login()
    start_up()
    return

system_operate_list["first_enter"] = True
system_operate_list["login"] = False
start_up()