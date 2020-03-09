import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


class MySQLConnectionPool:
    connectionPool = None

    @staticmethod
    def setupConnectionPool(self, poolName, poolSize, hostName, database, userName, passWord):
        try:
            self.connectionPool = mysql.connector.pooling.MySQLConnectionPool(pool_name=poolName,
                                                                              pool_size=poolSize,
                                                                              pool_reset_session=True,
                                                                              host=hostName,
                                                                              database=database,
                                                                              user=userName,
                                                                              password=passWord)
            print('Created a MySQL connection pool: ', self.connectionPool.pool_name, self.connectionPool.pool_size)
            return self.connectionPool
        except Error as e:
            print("Error when creating a MySQL connection", e.message)

    @staticmethod
    def getConnectionFromPool(self):
        try:
            conn = self.connectionPool.get_connection()
            if conn.is_connected():
                print('Created connection from pool: ', conn)
                return conn
        except Error as e:
            print("Error when creating a MySQL connection", e.message)

    @staticmethod
    def closeConnection(connection):
        try:
            if connection is not None and connection.is_connected():
                connection.close()
        except Error as e:
            print("Error when closing connection: ", e.message)
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                print("MySQL connection closed !")
