import logging
from AppCore.utils import MatplotlibHelper, AppLogger, ApiRequestLibUtils
from AppCore.database import MySQLConnectionPool
import pprint

class AppMain:
    LOGGER = AppLogger('AppMain')
    matplotlibHelper = None

    def __init__(self):
        self.matplotlibHelper = MatplotlibHelper()

    def showSimpleLine(self):
        self.matplotlibHelper.showLineChart('Simple line chart', 'X axis', 'yLabel', 8, 8, ['AA', 'BB', 'CC', 'DD'], [1, 4, 9, 16])

    def showAllMarkersInfo(self):
        self.LOGGER.logInfo('Show all Markers info of Matplotlib')
        self.matplotlibHelper.showAllMarkersInfo()

    def getConnectionFromPool(self):
        self.LOGGER.logInfo('Get Connection from MySQL Pool')
        myConnectionPool = MySQLConnectionPool()
        poolName = 'MySQL'
        poolSize = 4
        hostName = 'localhost'
        userName = 'XXXX'
        passWord = 'XXXX'
        database = 'DB_Schema'
        myConnectionPool.setupConnectionPool(self, poolName, poolSize, hostName, database, userName, passWord)
        # print('Created {} - {}', myConnectionPool.pool_name, myConnectionPool.pool_size)
        # print(connection_pool.pool_size)
        conn = myConnectionPool.getConnectionFromPool(self)
        if conn.is_connected():
            print(conn)
            cursor = conn.cursor()
            cursor.execute("select * from stock_info")
            record = cursor.fetchone()
            print("Your connected to - ", record)
            myConnectionPool.closeConnection(conn)

    def getRandomUsers(self):
        url = 'https://randomuser.me/api/?results=1'
        users = ApiRequestLibUtils.doGet(url)
        pprint.pprint(users)

################################################################
#       RUN APP
################################################################
appMain = AppMain()

"""
Display Line Chart
"""
# appMain.showSimpleLine()

# Show all markers' name and description in Matplotlib library
# appMain.showAllMarkersInfo()

# Test connect to MySQL database via connection pooling
# appMain.getConnectionFromPool()


# Test API using Requests lib & Pprint lib
# appMain.getRandomUsers()