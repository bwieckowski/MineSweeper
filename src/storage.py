class Storage(object):
    __instance = None
    dic = {}
    def __new__(self,):
        if Storage.__instance is None:
            Storage.__instance = object.__new__(self)
        return Storage.__instance

    def get(self, key):
        return self.dic[key]

    def add(self, key, value):
        self.dic[key] = value

    def allValue(self):
        return self.dic


if __name__ == "__main__":
    storage1 = Storage( )
    storage1.add("num",1)
    storage2 = Storage()
    storage2.add("test",2)
    print( storage1.allValue() )