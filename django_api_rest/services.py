class ResponseService():
    
    def __init__(self, data, success):
        self.__data__ = data
        self.__success__ = success


    def get_data(self):
        return self.__data__


    def get_success(self):
        return self.__success__
