import mysql.connector as m
import flask

mydb = m.connect(host = "localhost", user="root", password="Raviteja@01", database="loginpage1" )
#mydb = m.connect(host = "localhost", user="root", password="Raviteja@01", database="" )
mycursor = mydb.cursor()
#mycursor.execute("create database loginpage1")
'''
    till now we have conncted to the database (if the database is not created then uncomment the 5th and 7th line and comment the 4th line and after the connection is done undo the process that you have done now)
'''
#mycursor.execute("create table Accounts(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(100), password varchar(100), email varchar(100))")
'''

'''
mycursor.execute("show tables")
for i in mycursor:
    print(i)


