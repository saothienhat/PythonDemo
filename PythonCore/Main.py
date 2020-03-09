import pandas as pd
import postgres
import psycopg2
import mysql.connector

from mysql.connector import Error
from mysql.connector import pooling

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

connectionPoolName = 'testing'

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=connectionPoolName,
                                                                  pool_size=1,
                                                                  pool_reset_session=True,
                                                                  host=hostname,
                                                                  database=database,
                                                                  user=username,
                                                                  password=password)
    print('Created {} - {}' , connection_pool.pool_name, connection_pool.pool_size)
    # print(connection_pool.pool_size)
    conn = connection_pool.get_connection()
    if conn.is_connected:
        print(conn)
        cursor = conn.cursor()
        # cursor.execute('Select database()')
        # # data = cursor.fetchall
        # data = cursor.fetchone()
        # print(data)
        # cursor.execute("select database()")
        cursor.execute("select * from stock_info")
        record = cursor.fetchone()
        print("Your connected to - ", record)


except Error as e:
    print("DB exception: ", e.message)