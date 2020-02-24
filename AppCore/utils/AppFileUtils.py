import os


class AppFileUtils:

    @staticmethod
    def deleteFile(filePath):
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print('The file ' + filePath + ' does not exist !')
