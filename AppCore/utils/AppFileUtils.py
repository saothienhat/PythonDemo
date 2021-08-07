import os


class AppFileUtils:
    WRITE_IN_TEXT_MODE = 'w'
    READ_IN_TEXT_MODE = 'r'
    READ_WRITE_IN_BINARY_MODE = 'r+b'
    ENCODING_UTF8 = 'utf-8'

    @staticmethod
    def isExistFile(filePath):
        if os.path.exists(filePath): return True
        return False

    @staticmethod
    def deleteFile(filePath):
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print('The file ' + filePath + ' does not exist !')

    @staticmethod
    def deleteDir(folderPath):
        os.rmdir(folderPath)

    @staticmethod
    def openFile(filePath, mode=READ_IN_TEXT_MODE, encoding=ENCODING_UTF8):
        # Syntax
        # file_object = open(filename [,mode] [, isBuffering])
        # file opening example in Python
        try:
            fileOpener = open(filePath, mode, encoding)
            print("Result of reading file........")
            print("\tFile Name: ", fileOpener.name)
            print("\tMode of Opening: ", fileOpener.mode)
            print("\tIs Closed: ", fileOpener.closed)
            # print ("\tSoftspace flag : ", fo.softspace)
        finally:
            fileOpener.close()
