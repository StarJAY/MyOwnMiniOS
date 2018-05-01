import hashlib #To encode passwords
import math
import time

system_operate_list = {}
users = []
folders = {}
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
			system_operate_list["current_user"] = username
			print "Welcome",username
			print time.time()
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
  User:
	lst usr --- list saved users.
	new usr --- create a new user.
	
  Folder:
  	new folder --- create a new folder.
  	lst path --- list the folders in current path.
  	
  System:
	exit --- shutdown system.
	'''
	return
	
def list_users():
	length = len(users)
	for i in xrange(length):
		print "  User",i + 1,":",users[i]
	return
	
def move_to():
	path = raw_input("Move to:(home/system)")
	system_operate_list["current_path"] = path
	return 
	
def lst_path():
	print folders[system_operate_list["current_path"]]
	return
	
def create_folder():
	name = raw_input("FolderName:")
	path = raw_input("Path:")
	folders[path][name] = {"private":False}
	
def main(username):
	command = raw_input(">>>")
	if command == "help":
		print_help()
		main(username)
	elif command == "lst usr":
		list_users()
	elif command == "new usr":
		create_user()
	elif command == "moveto":
		move_to()
	elif command == "lst path":
		lst_path()
	elif command == "new folder":
		create_folder()
	elif command == "shut down" or "exit":
		system_operate_list["shuttingdown"] = True
	else:
		print "Unknown command..."
		main(username)
	return
	
def start_up():
	if system_operate_list["first_enter"] == True:
		print "Please create a new user:"
		create_user()
	else:
		if system_operate_list["login"] == False:
			login()
		else:
			main(system_operate_list["current_user"])
	if system_operate_list["shuttingdown"] == True:
		print "  Shutting down..."
		print "    Farewell..."
		pass
	else:
		start_up()
	return

system_operate_list["first_enter"] = True
system_operate_list["login"] = False
system_operate_list["current_path"] = "home"
system_operate_list["shuttingdown"] = False

folders["home"] = {"private":False}
folders["system"] = {"private":False}
folders["home"]["test"] = {}
folders["home"]["images"] = {}
folders["home"]["texts"] = {}

start_up()

