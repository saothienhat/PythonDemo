import pandas as pd
import postgres
import psycopg2
import mysql.connector

import requests
import pprint

data = {
    'x': [1, 2, 3],
    'y': [4, 5, 6]
}

# binh = pd.DataFrame(data)
# binh = pd.read_csv('d:/Album_202003021045.csv')
# print(binh)

hostname = 'localhost'
username = 'root'
password = 'root'
database = 'vnstock'

# def doQuery( conn ) :
#     cur = conn.cursor()
#     cur.execute( "SELECT * FROM album" )
#     for id in cur.fetchall() :
#         print(id)
#
# myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
# doQuery( myConnection )
# myConnection.close()

numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
cities = ['London', 'Dublin', 'Oslo']


url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
# pprint.pprint(users)
pprint.pprint(cities)
pprint.pprint(numbers)

