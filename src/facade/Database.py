import facade.Properties as properties

class Database:
    @staticmethod
    def getProperties(dbname):
        filename = dbname + ".txt"
        props = properties.parse(filename)
        return props
