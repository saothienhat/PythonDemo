
class DictionaryPy:
    dict = {}

    def __repr__(self):
        return 'This is Wrapper for Dictionary datatype in Python'

    def __init__(self, dictionary):
        self.dict = dictionary

    def getDataType(self):
        return 'Dictionary'

    def get(self):
        return self.dict

    def set(self, dictionary):
        self.dict = dictionary

    # Add item
    def put(self, key, value):
        self.dict[key] = value

    # Update item
    def update(self, key, value):
        self.dict[key] = value

    # Clear all
    def clear(self):
        self.dict.clear()

    # delete the dictionary itself
    def delete(self):
        del self.dict

    def getValueByKey(self, key):
        return self.dict.get(key)

    def clone(self):
        return self.dict.copy()

    # Delete an item from dictionary
    def deleteItemByKey(self, key):
        del [self.dict[key]]