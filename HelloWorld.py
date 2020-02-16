# Author:Anthony Quinn
# Description: A test project.
# Date: 16th February 2020

import datetime
import mysql.connector

todays_date = datetime.datetime.now()
print("Hello World on  the ", todays_date)

'''This is just to check that the second committe is working'''

'''What a day, what a stormy day'''

q_request = input("What day is it today:")
print("It's ??:", q_request)
