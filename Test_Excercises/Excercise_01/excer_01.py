"""
Exercise 1 (and Solution)

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

"""

import datetime

def excer_01():
	user_name = input("What is your nane")
	
	
	user_age = int(input("what is your age"))
	
	ydate_obj = datetime.date.today()
	
	print("{}, you will turn 100 in the year {}".format(user_name,ydate_obj.year + user_age))
	

	
excer_01()
